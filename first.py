import streamlit as st
st.title('学生米线🍜 数字档案')
st.header('✨基础信息')
st.text('学号：23031310110')
st.text("在读学校：广西职业师范学院",help='位于广西南宁市')
st.text('当前学习课程：大数据分析与应用实训     任课教师：陆紫光')
st.text('上课教室：实204')


import streamlit as st  # 导入Streamlit并用st代表它


st.subheader('收入情况')
st.metric(label="当月收入", value="1500", delta="0")

st.subheader('天气情况')
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="温度", value="24℃", delta="+2℃")
c2.metric(label="湿度", value="61%", delta="6%")
c3.metric(label="风速", value=None, delta="2", delta_color="off")

st.subheader('班级情况')
st.metric(label="班级人数", value="49", delta="0", label_visibility='hidden')


st.header('🎶个人爱好（听音乐）')


st.markdown(':blue[喜欢的歌手：周杰伦]7️⃣🍐🐘')

st.header('简单代码展示🔥')
str = '''
a=2
b=3
print(a*b)'''

st.code(str,language='python',line_numbers=True)
st.caption('这是python代码')
st.markdown('***')
