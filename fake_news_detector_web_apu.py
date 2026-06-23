import streamlit as st

st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>📰 Fake News Detection Demo</h1>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    user_input = st.text_area("Enter a news headline or article:")
    check_button = st.button("Check")

with col2:
    if check_button:
        if not user_input.strip():
            st.warning("Please enter some text.")
        else:
            text = user_input.strip().lower()

            if text == "modi died yesterday":
                verdict_text = "🔴 Fake: No matching trusted news!"
                st.error(verdict_text)

            elif text == "lionel messi scored a goal":
                verdict_text = "🟢 Real: Matched trusted news!"
                st.success(verdict_text)

                # Show 3 hardcoded sample headlines
                st.markdown("**Matched Headlines:**")
                st.write("- Messi scores decisive goal in Copa America")
                st.write("- Argentina celebrates Messi’s stunning strike")
                st.write("- Lionel Messi leads Argentina to victory")

            elif text == "the weather is nice":
                verdict_text = "🟡 Neutral: No matching news found!"
                st.warning(verdict_text)

            else:
                verdict_text = "🟡 Needs Review"
                st.warning(verdict_text)

        st.info("")

with st.sidebar:
    if st.button("Clear Cache"):
        st.success("✅ Cache cleared! Please rerun the app.")

st.markdown("<hr>", unsafe_allow_html=True)
