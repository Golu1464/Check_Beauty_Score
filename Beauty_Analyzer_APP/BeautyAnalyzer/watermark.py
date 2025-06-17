# def add_footer():
# 	import streamlit as st
# 	st.markdown("""
# 		<style>
# 			.footer {
# 				position: fixed;
# 				left: 0;
# 				bottom: 0;
# 				width: 100%;
# 				background-color: #f0f2f6;
# 				color: #444;
# 				text-align: center;
# 				padding: 10px;
# 				font-size: 14px;
# 				z-index: 9999;
# 			}
# 		</style>
# 		<div class="footer">
# 			🚀 Made with ❤️ by <b>Sonu Kumar</b> |
# 			<a href="https://github.com/Golu1464" target="_blank">GitHub</a> |
# 			<a href="https://linkedin.com/in/your-profile" target="_blank">LinkedIn</a>
# 		</div>
# 	""", unsafe_allow_html=True)

def add_header():
    import streamlit as st
    st.markdown("""
        <div style='
            text-align: center;
            padding: 10px;
            background-color: #1f2937;
            color: #f9fafb;
            border-radius: 12px;
            margin-bottom: 25px;
            font-size: 16px;
        '>
            🔖 Built by <b style='color:#3B82F6;'>Sonu Kumar Sharma</b> — 
            <a href='https://github.com/Golu1464' target='_blank' style='color: #60A5FA; text-decoration: none;'>GitHub</a> |
            <a href='https://linkedin.com/in/your-profile' target='_blank' style='color: #60A5FA; text-decoration: none;'>LinkedIn</a>
        </div>
    """, unsafe_allow_html=True)
