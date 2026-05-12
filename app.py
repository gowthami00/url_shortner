import streamlit as st
import pyshorteners
import pyperclip

st.set_page_config(page_title="URL Shortener", page_icon="🔗", layout="centered")

st.title("🔗 URL Shortener")
st.write("Convert your long URLs into short, shareable links instantly!")

# Input
long_url = st.text_input("Enter your long URL:", placeholder="https://www.example.com/very/long/url")

col1, col2 = st.columns(2)

with col1:
    service = st.selectbox("Choose service:", ["TinyURL", "Clckru"])

if st.button("Shorten URL ✂️", use_container_width=True):
    if long_url:
        if not long_url.startswith("http"):
            st.error("Please enter a valid URL starting with http:// or https://")
        else:
            with st.spinner("Shortening..."):
                try:
                    s = pyshorteners.Shortener()
                    if service == "TinyURL":
                        short_url = s.tinyurl.short(long_url)
                    else:
                        short_url = s.clckru.short(long_url)

                    st.success("✅ URL Shortened Successfully!")

                    st.markdown("### Your Short URL:")
                    st.code(short_url)

                    # Save to history
                    if "history" not in st.session_state:
                        st.session_state.history = []
                    st.session_state.history.append({
                        "Original": long_url[:50] + "...",
                        "Short URL": short_url
                    })

                except Exception as e:
                    st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a URL first!")

# History
if "history" in st.session_state and st.session_state.history:
    st.divider()
    st.subheader("📋 History")
    for item in reversed(st.session_state.history):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write(f"🔗 {item['Original']}")
        with col2:
            st.code(item["Short URL"])

st.divider()
st.markdown("Made with by Gowthami")