
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import io
import base64
plt.rcParams['font.family'] = 'AppleGothic'



st.set_page_config(page_title='recc',layout='wide')

df = pd.read_csv('/Users/jeong-yula/Desktop/streamlit/��ó����������.csv')
df_plus=pd.read_csv('/Users/jeong-yula/Desktop/streamlit/hs_plus.csv')
df_tool=pd.read_csv('/Users/jeong-yula/Desktop/streamlit/tool1.csv')
# hardskill_df=pd.read_csv('/Users/jeong-yula/Desktop/streamlit/hardskill.csv')



tab1, tab2, tab3, tab4 = st.tabs(["recommend", "trend", "etc","��� ����"])

with tab1:   
    # col1, col2 = st.columns(2)

    st.header('Hard Skill')
    st.write("DA : ������ �м� ��ü�� ���� ����")
    st.write("��� : ��� �м�, ����� ����, ȸ�� �м�, ������ �м� ��")
    st.write("�ӽŷ��� : �ӽŷ���, �𵨸�, �з�/���� �𵨸�, �ð迭 ������ Ȱ��")
    st.write("������ : ������, �˰���, �����ӿ�ũ, �˻� �˰���, ��õ �˰���, �ڿ��� ó��, ���� �𵨸�")
    st.write("�ð�ȭ : ������ �ð�ȭ, BI Tool Ȱ��, ��ú��� ����")
    st.write("������ ���� : ������ ����, ������ ����, ������ ó��")
    st.write("������ : ������ �м�, ������ ó��, ��뷮 ������ �л�ó�� ����")
    st.write("Ŭ���� : Ŭ���� ���� �÷��� (AWS, GA4, Google Cloud Platform ��)")
    st.write("���������� : �����͸�Ʈ, ������ �����Ͽ콺, ������ ����ũ ���� �� ������ ���������� ���� ����")
    st.write("�׷ν� ��ŷ : Funnel �м�, Cohort �м�, AARRR, Retention, A/B�׽�Ʈ �� ������ �� ����Ͻ� �м��� �ʿ��� �м� ��� Ȱ�� ����")
    st.write("�α� : App/Web ���� ������, ����� �ൿ ������, �α� ������")
    st.write("������ : ������ ����, ���δ�Ʈ �м�, ����Ͻ� �м�")
        
    hardskill=st.multiselect(
        'select hard skill',
        ['DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����',
            '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������']
        )




    st.header('���')
    option = st.selectbox(
        "��� �Ⱓ",
        ("1", "2", "3","4","5","6","7"),
        index=None
    )

    st.write('You selected:', option)



    start=st.button('��õ �ޱ�')

    if start:
    # df_filtered=df.loc[df['Tool'].isin(lang),:]
        filtered_df = df[(df[hardskill] == 1).any(axis=1)]
        first_row = filtered_df.iloc[0]
        index = filtered_df.index[0]

    # st.dataframe(data=filtered_df)

        selected_columns = ['Unnamed: 0', 'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����',
        '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������']
        new_df = filtered_df[selected_columns]




        from sklearn.metrics.pairwise import cosine_similarity


        cosine_sim = cosine_similarity(new_df)

        def cos_sim_index(index_num):
            selected_similarities = cosine_sim[int(index_num)]
            similarities_with_index = [(similarity, index) for index, similarity in enumerate(selected_similarities) if index != int(index_num)]
            similarities_with_index.append((1.0, int(index_num)))  # Add similarity of 1.0 for the selected index
            sorted_similarities = sorted(similarities_with_index, key=lambda x: x[0], reverse=True)
            top_6_similar_jobs = [filtered_df.iloc[index].tolist() for similarity, index in sorted_similarities[:6]]

            df = pd.DataFrame(data = top_6_similar_jobs,columns=['Unnamed: 0', '����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����', '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������', '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ', 'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����', '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������', '������', '���α׷��־��', '�ǻ����', '����/�м��� ���', '�����ذ�ɷ�', '���μ���', '������', 'å�Ӱ�', '������', '����/����', 'â�Ƿ�', '����Ͻ�', '�׼ǵ���', 'Agile', '����', '����/����', 'Tool1', 'SQL', 'Python', 'R', '�ð�ȭ ��', '�α׺м�', 'BigData', 'Cloud', 'database', '����', 'MLtool', 'DLtool', 'DA plus', '��� plus', 'ML plus', 'DL plus', '�ð�ȭ plus', '������ ���� plus', '������ plus', '���������� plus', '�׷ν���ŷ plus', '�α� plus', '������ plus', '�ǻ���� plus', '������ plus', '�����ذ�ɷ� plus', 'Agile plus', '�з� plus', 'â�Ƿ� plus', '������ plus', '����/�м��� ��� plus', '����/���� plus', '���� plus', '����', '������', '������Ʈ ����', '��', 'tool plus1', 'SQL plus', 'Python plus', 'R plus', '�ð�ȭ �� plus', '�α׺м� plus', 'BigData plus', 'Cloud plus', 'database plus', '���� plus', 'MLTool plus', 'DLTool plus']
            )

            df=df[['����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', 
                    '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 
                    'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����',
                        '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', 
                        '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������',
                        '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                    '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ'
                    ,'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����',
                '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������']]

            st.header('����5��')
            st.dataframe(data=df)

        cos_sim_index(index)

        # ������
        filtered_df_plus = df_plus[(df_plus[hardskill] == 1).all(axis=1)]
        first_row_plus = filtered_df_plus.iloc[0]
        index_plus = filtered_df_plus.index[0]

        selected_columns = ['Unnamed: 0', 'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����',
            '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������']
        new_df_plus = filtered_df_plus[selected_columns]

        cosine_sim = cosine_similarity(new_df_plus)

        def cos_sim_index(index_num):
            selected_similarities = cosine_sim[int(index_num)]
            similarities_with_index = [(similarity, index) for index, similarity in enumerate(selected_similarities) if index != int(index_num)]
            similarities_with_index.append((1.0, int(index_num)))  # Add similarity of 1.0 for the selected index
            sorted_similarities = sorted(similarities_with_index, key=lambda x: x[0], reverse=True)
            top_6_similar_jobs = [filtered_df_plus.iloc[index].tolist() for similarity, index in sorted_similarities[:6]]

            df_plus = pd.DataFrame(data = top_6_similar_jobs,columns=['Unnamed: 0','Unnamed: 0', '����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����', '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������', '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ', 'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����', '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������', '������', '���α׷��־��', '�ǻ����', '����/�м��� ���', '�����ذ�ɷ�', '���μ���', '������', 'å�Ӱ�', '������', '����/����', 'â�Ƿ�', '����Ͻ�', '�׼ǵ���', 'Agile', '����', '����/����', 'Tool1', 'SQL', 'Python', 'R', '�ð�ȭ ��', '�α׺м�', 'BigData', 'Cloud', 'database', '����', 'MLtool', 'DLtool', 'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����', '������', '����������', '�׷ν���ŷ', '�α�', '������', '�ǻ���� plus', '������ plus', '�����ذ�ɷ� plus', 'Agile plus', '�з� plus', 'â�Ƿ� plus', '������ plus', '����/�м��� ��� plus', '����/���� plus', '���� plus', '����', '������', '������Ʈ ����', '��', 'tool plus1', 'SQL plus', 'Python plus', 'R plus', '�ð�ȭ �� plus', '�α׺м� plus', 'BigData plus', 'Cloud plus', 'database plus', '���� plus', 'MLTool plus', 'DLTool plus']
        )

            df_plus=df_plus[['����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', 
                '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 
                'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����',
                    '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', 
                    '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������',
                    '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ']]

            st.header('������ 5��')
            st.dataframe(data=df_plus)

        cos_sim_index(index_plus)



with tab2:
   st.header("Trend")

   with st.container():
      st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

   st.write("This is outside the container")

with tab3:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Soft Skill')
        softskill=st.multiselect(
            'soft skill ����',
            ['�ǻ����', '����/�м��� ���', '�����ذ�ɷ�', '���μ���', '������', 'å�Ӱ�', 
             '������', '����/����', 'â�Ƿ�', '����Ͻ�', '�׼ǵ���', 'Agile', '����', '����/����']
            )
        start1=st.button('���� ���� Ȯ���ϱ�',key='1')
        if start1:
            filtered_softskill= df[(df[softskill] == 1).all(axis=1)]

            
            filtered_softskill=filtered_softskill[['����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', 
                   '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 
                   'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����',
                     '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', 
                     '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������',
                       '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                   '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ']]
            st.dataframe(data=filtered_softskill)

    with col2:
        st.header('������')
        domain=st.multiselect(
            '���� ������ ����',
            ['����', '�װ�', '������', '���� ����', '����', 'ä��', '���� ����Ʈ���� ����', '������', '�Ƿ�',
       '������', '��Ŀ�ӽ�', '�����Ƽ', '�������θ�Ʈ', '����', '�ǰ�', '����', '�м�', '���� ���񽺾�',
       '����', '����', '�ְ�', '����', '���', '��ǰ', '����', '����', '����', '���', '�ε���',
       '����', '����ġ', '���', 'ȯ��', '�ý��� ����Ʈ���� ����', '������', 'ȭ��ǰ', '�Ҽ� ��Ʈ��ũ',
       'Ŭ���� ��ǻ��'])
      
        start2=st.button('���� ���� Ȯ���ϱ�',key='2')
        if start2:
            filtered_domain=df.loc[df["����� ��ó��"].isin(domain),:]

            filtered_domain=filtered_domain[['����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', 
                   '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 
                   'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����',
                     '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', 
                     '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������',
                       '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                   '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ']]
                    
            st.dataframe(data=filtered_domain)

    with col3:
        st.header('TOOL')
        tool=st.multiselect('Tool ����',
                            ['sql','r','python','tableau','redash','powerbi','lookerstudio','googleanalytics','amplitude','hadoop','hive'
                             ,'airflow','bigquery','aws','spark','pytorch','tensorflow']
        )
        start3=st.button('���� ���� Ȯ���ϱ�',key='3')

        if start3:
            filtered_tool=df_tool.loc[df_tool["Tool"].isin(tool),:]
            filtered_tool=filtered_tool[['����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', 
                   '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 
                   'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����',
                     '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', 
                     '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������',
                       '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                   '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ']]
            
            st.dataframe(data=filtered_tool)

with tab4:

    df_etc=df[['����̸�','�������̸�','������','ä������','�ٹ����','����Ұ�','�ڰݿ��','������','����','�ֿ����',
           '����', '��� ��', '��� ��� ����', '�������',
                       '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                   '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�',
                   '���','�Ի�']]
    
    
    
    selected_info = df_etc.iloc[5]
    company_name = selected_info['����̸�']
    scores = selected_info[['����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ']]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(scores.index, scores.values, color='green')
    ax.set_title(f'{company_name} ���� ������ ��ǥ')
    ax.set_xlabel('��ǥ')
    ax.set_ylabel('������')
    ax.set_ylim(0, 5)  # �������� 0���� 5 ������ ��
    
    st.pyplot(fig)

    # st.write(selected_info)

    # columns = ['����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ']
    # values = selected_info[['����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ']]

    # # �� ��Ʈ�� �׸��� ���� �����͸� ��ųʸ� ���·� ��ȯ
    # data = {columns[i]: values[i] for i in range(len(columns))}


#     #�����
#     df_name=selected_info['����̸�']
#     st.header("�����")
#     st.write(df_name)

#     st.divider()  

#     # �ֿ����
#     df_work=selected_info['�ֿ����']
#     st.header("�ֿ� ����")
#     st.write(df_work)

#     st.divider()  

#     # �ڰݿ��
#     df_intro=selected_info['�ڰݿ��']
#     st.header("�ڰ� ���")
#     st.write(df_intro)

#     st.divider()  

#     # �ڰݿ��
#     df_pplus=selected_info['������']
#     st.header("��� ����")
#     st.write(df_pplus)

#     st.divider()  

#     # �����
#     df_rev=selected_info['�����']
#     st.header("�����")
#     st.write(df_rev)

#     st.divider()  

#     # ����� 
#     df_ppl=selected_info['��� ��']
#     st.header("��� ��")
#     st.write(df_ppl,"��")

#     st.divider()  

#     # �����տ���
#     df_income=selected_info['��� ��� ����']
#     st.header("��� ��� ����")
#     st.write(df_income,"����")

#     st.divider()  

#     # ����Ի��� �� 
#     df_out=selected_info['���']
#     df_in=selected_info['�Ի�']
#     st.header("�۳� ���/�Ի��� ��")
#     st.write(df_out,"/",df_in)

#     st.divider()  

#     st.header("��� ����")

#     bar_chart_data = pd.DataFrame({
#         'aspect': ['����', '���� �� �޿�', '�����', '�系��ȭ', '���� ��ȸ'],
#         'score': selected_info[['����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ']]
#     })

#     # �� ��Ʈ ����
#     bar_chart = alt.Chart(bar_chart_data).mark_bar(color='gray').encode(
#         x=alt.X('aspect:N', title=None, axis=alt.Axis(labelAngle=0)),
#         y=alt.Y('score:Q', title='Score'),
#         tooltip=['aspect:N', 'score:Q']
#     ).properties(
#         width=alt.Step(80),
#         height=400
#     )

#     st.altair_chart(bar_chart, use_container_width=True)

#     st.divider()  

#     chart_data = pd.DataFrame({
#     'aspect': ['�����õ��', 'CEO ������', '���� ���ɼ�'],
#     'score': selected_info[['�����õ��', 'CEO ������', '���� ���ɼ�']]
# })

#     # �� �׷��� ����
#     line_chart = alt.Chart(chart_data).mark_bar().encode(
#         x=alt.X('aspect:N', title=None, axis=alt.Axis(labelAngle=0)),
#         y=alt.Y('score:Q', title='Score (%)'),
#         tooltip=['aspect:N', 'score:Q']
#     ).properties(
#         width=alt.Step(80),
#         height=400
#     )

#     st.altair_chart(line_chart, use_container_width=True)



import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import io
import base64
plt.rcParams['font.family'] = 'AppleGothic'



st.set_page_config(page_title='recc',layout='wide')

df = pd.read_csv('/Users/jeong-yula/Desktop/streamlit/��ó����������.csv')
df_plus=pd.read_csv('/Users/jeong-yula/Desktop/streamlit/hs_plus.csv')
df_tool=pd.read_csv('/Users/jeong-yula/Desktop/streamlit/tool2.csv')
# hardskill_df=pd.read_csv('/Users/jeong-yula/Desktop/streamlit/hardskill.csv')



tab1, tab2, tab3, tab4 = st.tabs(["recommend", "trend", "etc","��� ����"])

with tab1:   
    # col1, col2 = st.columns(2)

    st.header('Hard Skill')
    st.write("DA : ������ �м� ��ü�� ���� ����")
    st.write("��� : ��� �м�, ����� ����, ȸ�� �м�, ������ �м� ��")
    st.write("�ӽŷ��� : �ӽŷ���, �𵨸�, �з�/���� �𵨸�, �ð迭 ������ Ȱ��")
    st.write("������ : ������, �˰���, �����ӿ�ũ, �˻� �˰���, ��õ �˰���, �ڿ��� ó��, ���� �𵨸�")
    st.write("�ð�ȭ : ������ �ð�ȭ, BI Tool Ȱ��, ��ú��� ����")
    st.write("������ ���� : ������ ����, ������ ����, ������ ó��")
    st.write("������ : ������ �м�, ������ ó��, ��뷮 ������ �л�ó�� ����")
    st.write("Ŭ���� : Ŭ���� ���� �÷��� (AWS, GA4, Google Cloud Platform ��)")
    st.write("���������� : �����͸�Ʈ, ������ �����Ͽ콺, ������ ����ũ ���� �� ������ ���������� ���� ����")
    st.write("�׷ν� ��ŷ : Funnel �м�, Cohort �м�, AARRR, Retention, A/B�׽�Ʈ �� ������ �� ����Ͻ� �м��� �ʿ��� �м� ��� Ȱ�� ����")
    st.write("�α� : App/Web ���� ������, ����� �ൿ ������, �α� ������")
    st.write("������ : ������ ����, ���δ�Ʈ �м�, ����Ͻ� �м�")
        
    hardskill=st.multiselect(
        'select hard skill',
        ['DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����',
            '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������']
        )




    st.header('���')
    option = st.selectbox(
        "��� �Ⱓ",
        ("1", "2", "3","4","5","6","7"),
        index=None
    )

    st.write('You selected:', option)



    start=st.button('��õ �ޱ�')

    if start:
    # df_filtered=df.loc[df['Tool'].isin(lang),:]
        filtered_df = df[(df[hardskill] == 1).any(axis=1)]
        first_row = filtered_df.iloc[0]
        index = filtered_df.index[0]

    # st.dataframe(data=filtered_df)

        selected_columns = ['Unnamed: 0', 'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����',
        '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������']
        new_df = filtered_df[selected_columns]




        from sklearn.metrics.pairwise import cosine_similarity


        cosine_sim = cosine_similarity(new_df)

        def cos_sim_index(index_num):
            selected_similarities = cosine_sim[int(index_num)]
            similarities_with_index = [(similarity, index) for index, similarity in enumerate(selected_similarities) if index != int(index_num)]
            similarities_with_index.append((1.0, int(index_num)))  # Add similarity of 1.0 for the selected index
            sorted_similarities = sorted(similarities_with_index, key=lambda x: x[0], reverse=True)
            top_6_similar_jobs = [filtered_df.iloc[index].tolist() for similarity, index in sorted_similarities[:6]]

            df = pd.DataFrame(data = top_6_similar_jobs,columns=['Unnamed: 0', '����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����', '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������', '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ', 'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����', '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������', '������', '���α׷��־��', '�ǻ����', '����/�м��� ���', '�����ذ�ɷ�', '���μ���', '������', 'å�Ӱ�', '������', '����/����', 'â�Ƿ�', '����Ͻ�', '�׼ǵ���', 'Agile', '����', '����/����', 'Tool1', 'SQL', 'Python', 'R', '�ð�ȭ ��', '�α׺м�', 'BigData', 'Cloud', 'database', '����', 'MLtool', 'DLtool', 'DA plus', '��� plus', 'ML plus', 'DL plus', '�ð�ȭ plus', '������ ���� plus', '������ plus', '���������� plus', '�׷ν���ŷ plus', '�α� plus', '������ plus', '�ǻ���� plus', '������ plus', '�����ذ�ɷ� plus', 'Agile plus', '�з� plus', 'â�Ƿ� plus', '������ plus', '����/�м��� ��� plus', '����/���� plus', '���� plus', '����', '������', '������Ʈ ����', '��', 'tool plus1', 'SQL plus', 'Python plus', 'R plus', '�ð�ȭ �� plus', '�α׺м� plus', 'BigData plus', 'Cloud plus', 'database plus', '���� plus', 'MLTool plus', 'DLTool plus']
            )

            df=df[['����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', 
                    '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 
                    'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����',
                        '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', 
                        '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������',
                        '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                    '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ'
                    ,'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����',
                '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������']]

            st.header('����5��')
            st.dataframe(data=df)

        cos_sim_index(index)

        # ������
        filtered_df_plus = df_plus[(df_plus[hardskill] == 1).all(axis=1)]
        first_row_plus = filtered_df_plus.iloc[0]
        index_plus = filtered_df_plus.index[0]

        selected_columns = ['Unnamed: 0', 'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����',
            '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������']
        new_df_plus = filtered_df_plus[selected_columns]

        cosine_sim = cosine_similarity(new_df_plus)

        def cos_sim_index(index_num):
            selected_similarities = cosine_sim[int(index_num)]
            similarities_with_index = [(similarity, index) for index, similarity in enumerate(selected_similarities) if index != int(index_num)]
            similarities_with_index.append((1.0, int(index_num)))  # Add similarity of 1.0 for the selected index
            sorted_similarities = sorted(similarities_with_index, key=lambda x: x[0], reverse=True)
            top_6_similar_jobs = [filtered_df_plus.iloc[index].tolist() for similarity, index in sorted_similarities[:6]]

            df_plus = pd.DataFrame(data = top_6_similar_jobs,columns=['Unnamed: 0','Unnamed: 0', '����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����', '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������', '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ', 'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����', '������', 'Ŭ����', '����������', '�׷ν���ŷ', '�α�', '������', '������', '���α׷��־��', '�ǻ����', '����/�м��� ���', '�����ذ�ɷ�', '���μ���', '������', 'å�Ӱ�', '������', '����/����', 'â�Ƿ�', '����Ͻ�', '�׼ǵ���', 'Agile', '����', '����/����', 'Tool1', 'SQL', 'Python', 'R', '�ð�ȭ ��', '�α׺м�', 'BigData', 'Cloud', 'database', '����', 'MLtool', 'DLtool', 'DA', '���', 'ML', 'DL', '�ð�ȭ', '������ ����', '������', '����������', '�׷ν���ŷ', '�α�', '������', '�ǻ���� plus', '������ plus', '�����ذ�ɷ� plus', 'Agile plus', '�з� plus', 'â�Ƿ� plus', '������ plus', '����/�м��� ��� plus', '����/���� plus', '���� plus', '����', '������', '������Ʈ ����', '��', 'tool plus1', 'SQL plus', 'Python plus', 'R plus', '�ð�ȭ �� plus', '�α׺м� plus', 'BigData plus', 'Cloud plus', 'database plus', '���� plus', 'MLTool plus', 'DLTool plus']
        )

            df_plus=df_plus[['����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', 
                '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 
                'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����',
                    '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', 
                    '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������',
                    '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ']]

            st.header('������ 5��')
            st.dataframe(data=df_plus)

        cos_sim_index(index_plus)



with tab2:
   st.header("Trend")

   with st.container():
      st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

   st.write("This is outside the container")

with tab3:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Soft Skill')
        softskill=st.multiselect(
            'soft skill ����',
            ['�ǻ����', '����/�м��� ���', '�����ذ�ɷ�', '���μ���', '������', 'å�Ӱ�', 
             '������', '����/����', 'â�Ƿ�', '����Ͻ�', '�׼ǵ���', 'Agile', '����', '����/����']
            )
        start1=st.button('���� ���� Ȯ���ϱ�',key='1')
        if start1:
            filtered_softskill= df[(df[softskill] == 1).all(axis=1)]

            
            filtered_softskill=filtered_softskill[['����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', 
                   '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 
                   'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����',
                     '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', 
                     '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������',
                       '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                   '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ']]
            st.dataframe(data=filtered_softskill)

    with col2:
        st.header('������')
        domain=st.multiselect(
            '���� ������ ����',
            ['����', '�װ�', '������', '���� ����', '����', 'ä��', '���� ����Ʈ���� ����', '������', '�Ƿ�',
       '������', '��Ŀ�ӽ�', '�����Ƽ', '�������θ�Ʈ', '����', '�ǰ�', '����', '�м�', '���� ���񽺾�',
       '����', '����', '�ְ�', '����', '���', '��ǰ', '����', '����', '����', '���', '�ε���',
       '����', '����ġ', '���', 'ȯ��', '�ý��� ����Ʈ���� ����', '������', 'ȭ��ǰ', '�Ҽ� ��Ʈ��ũ',
       'Ŭ���� ��ǻ��'])
      
        start2=st.button('���� ���� Ȯ���ϱ�',key='2')
        if start2:
            filtered_domain=df.loc[df["����� ��ó��"].isin(domain),:]

            filtered_domain=filtered_domain[['����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', 
                   '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 
                   'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����',
                     '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', 
                     '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������',
                       '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                   '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ']]
                    
            st.dataframe(data=filtered_domain)

    with col3:
        st.header('TOOL')
        tool=st.multiselect('Tool ����',
                            ['sql','r','python','tableau','redash','powerbi','lookerstudio','googleanalytics','amplitude','hadoop','hive'
                             ,'airflow','bigquery','aws','spark','pytorch','tensorflow']
        )
        start3=st.button('���� ���� Ȯ���ϱ�',key='3')

        if start3:
            filtered_tool=df_tool.loc[df_tool["Tool"].isin(tool),:]
            filtered_tool=filtered_tool[['����Ʈ', '�˻� Ű����', '����̸�', '�������̸�', '�������̸� ��ó��', '������ ���� ', '������', 
                   '��� ä�� ����', '���_min', '���_max', '�з�', '�з� ��������', '��ų', '���⼭��', 'ä������', 'ä������', 
                   'ä������_��ó��', 'ä������_��ó�� ����', '�޿�', '�ٹ��ð�', '�ٹ����', '�ٹ���� ��', '�ٹ���� ��', '��⵵ �� ', '�ٹ�����',
                     '�ֿ����', '�����', '�ڰݿ��', 'Hard Skill', 'Soft Skill', 'Tool', '������', 'hard plus', 'soft plus', 'tool plus', 
                     '����', '����Ұ�', 'ǥ�ػ���з�', '�ֿ���', '�ֿ���.1', '�����', '����� ��ó��', '����', '��� ��', '��� ��� ����', '�������',
                       '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                   '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�', '���̶���Ʈ+�±�', '���', '�Ի�', '��ũ']]
            
            st.dataframe(data=filtered_tool)

with tab4:

    df_etc=df[['����̸�','�������̸�','������','ä������','�ٹ����','����Ұ�','�ڰݿ��','������','����','�ֿ����',
           '����', '��� ��', '��� ��� ����', '�������',
                       '��� ���� ��ó��', '��� ���� ��ó�� _����', '�����', '�������', '����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ', 
                   '�濵��', '�����õ��', 'CEO ������', '���� ���ɼ�',
                   '���','�Ի�']]
    
    
    
    selected_info = df_etc.iloc[5]
    company_name = selected_info['����̸�']
    scores = selected_info[['����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ']]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(scores.index, scores.values, color='green')
    ax.set_title(f'{company_name} ���� ������ ��ǥ')
    ax.set_xlabel('��ǥ')
    ax.set_ylabel('������')
    ax.set_ylim(0, 5)  # �������� 0���� 5 ������ ��
    
    st.pyplot(fig)

    # st.write(selected_info)

    # columns = ['����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ']
    # values = selected_info[['����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ']]

    # # �� ��Ʈ�� �׸��� ���� �����͸� ��ųʸ� ���·� ��ȯ
    # data = {columns[i]: values[i] for i in range(len(columns))}


#     #�����
#     df_name=selected_info['����̸�']
#     st.header("�����")
#     st.write(df_name)

#     st.divider()  

#     # �ֿ����
#     df_work=selected_info['�ֿ����']
#     st.header("�ֿ� ����")
#     st.write(df_work)

#     st.divider()  

#     # �ڰݿ��
#     df_intro=selected_info['�ڰݿ��']
#     st.header("�ڰ� ���")
#     st.write(df_intro)

#     st.divider()  

#     # �ڰݿ��
#     df_pplus=selected_info['������']
#     st.header("��� ����")
#     st.write(df_pplus)

#     st.divider()  

#     # �����
#     df_rev=selected_info['�����']
#     st.header("�����")
#     st.write(df_rev)

#     st.divider()  

#     # ����� 
#     df_ppl=selected_info['��� ��']
#     st.header("��� ��")
#     st.write(df_ppl,"��")

#     st.divider()  

#     # �����տ���
#     df_income=selected_info['��� ��� ����']
#     st.header("��� ��� ����")
#     st.write(df_income,"����")

#     st.divider()  

#     # ����Ի��� �� 
#     df_out=selected_info['���']
#     df_in=selected_info['�Ի�']
#     st.header("�۳� ���/�Ի��� ��")
#     st.write(df_out,"/",df_in)

#     st.divider()  

#     st.header("��� ����")

#     bar_chart_data = pd.DataFrame({
#         'aspect': ['����', '���� �� �޿�', '�����', '�系��ȭ', '���� ��ȸ'],
#         'score': selected_info[['����', '���� �� �޿�', '������ ���� ����', '�系��ȭ', '���� ��ȸ']]
#     })

#     # �� ��Ʈ ����
#     bar_chart = alt.Chart(bar_chart_data).mark_bar(color='gray').encode(
#         x=alt.X('aspect:N', title=None, axis=alt.Axis(labelAngle=0)),
#         y=alt.Y('score:Q', title='Score'),
#         tooltip=['aspect:N', 'score:Q']
#     ).properties(
#         width=alt.Step(80),
#         height=400
#     )

#     st.altair_chart(bar_chart, use_container_width=True)

#     st.divider()  

#     chart_data = pd.DataFrame({
#     'aspect': ['�����õ��', 'CEO ������', '���� ���ɼ�'],
#     'score': selected_info[['�����õ��', 'CEO ������', '���� ���ɼ�']]
# })

#     # �� �׷��� ����
#     line_chart = alt.Chart(chart_data).mark_bar().encode(
#         x=alt.X('aspect:N', title=None, axis=alt.Axis(labelAngle=0)),
#         y=alt.Y('score:Q', title='Score (%)'),
#         tooltip=['aspect:N', 'score:Q']
#     ).properties(
#         width=alt.Step(80),
#         height=400
#     )

#     st.altair_chart(line_chart, use_container_width=True)

