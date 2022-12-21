from django.shortcuts import render, HttpResponse
from .models import lodges
from checklist.models import checklist,features
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import plot

# Create your views here.
def index(request):
    return render(request,'lodge_page.html')

def report(request):
    if request.user.is_authenticated:
        user = request.user
        lodge = lodges.objects.get(user_id= user.id)
        #사용해야하 checklist 인스턴스들 호출
        checklist_use = checklist.objects.filter(lodge_id = lodge.id).values().order_by('id').last()
        last_day = checklist_use['check_date']
        checklist_need = checklist.objects.filter(lodge_id = lodge.id)
        if checklist_need.count() == 0:
            test = checklist_need.count()
            context = {'test' : test}
        else:
            checklist_need = checklist_need.filter(check_date = last_day).values()

            #checklist_safe
            checklist_safe = [[val for val in instance.values()][7:27].count('O') for instance in checklist_need ]
            len_safe = len(checklist_safe)
            cnt_safe = checklist_safe.count(20)

            #checklist_clean
            checklist_clean = [[val for val in instance.values()][27:] for instance in checklist_need ]
            checklist_clean = list(zip(*checklist_clean))
            room_cnt = len(checklist_clean[0])
            checklist_clean = [ val.count('O') for val in checklist_clean]
            

            #청결 도넛 그래프
            label = ['양호','미흡']
            values_clean = [checklist_clean.count(room_cnt), len(checklist_clean)-checklist_clean.count(room_cnt)]
            fig2 = go.Figure(data=[go.Pie(labels=label, values=values_clean, hole=.3)])
            fig2.update_layout(
            annotations=[dict(text='청결', font_size=20, showarrow=False)])
            layout_clean = {
            'title': '청결항목',
            'height': 150,
            'width': 150,
            }
            fig_clean = plot({'data': fig2,'layout': layout_clean}, output_type='div')



            context = {'fig_clean':fig_clean,
                        'len_safe':len_safe,
                        'cnt_safe':cnt_safe,
                        } 
    return render(request, 'report_main.html', context)

def info(request):
    if request.user.is_authenticated:
        user = request.user
        lodge = lodges.objects.get(user_id= user.id)
    return render(request, 'lodge_info.html', {'lodge':lodge})

def clean(request):
    if request.user.is_authenticated:
        user = request.user
        lodge = lodges.objects.get(user_id= user.id)
        checklist_use = checklist.objects.filter(lodge_id = lodge.id).values().order_by('id').last()

        #사용해야하 checklist 인스턴스들 호출
        checklist_use = checklist.objects.filter(lodge_id = lodge.id).values().order_by('id').last()
        last_day = checklist_use['check_date']
        checklist_need = checklist.objects.filter(lodge_id = lodge.id)
        checklist_need = checklist_need.filter(check_date = last_day).values()

        #객실 바 그래프 
        label = [val['room_num'] for val in checklist_need]
        fig1 = go.Figure(data=[go.Bar(
                x = [val['room_num'] for val in checklist_need],
                y= [round(([val for val in instance.values()][27:39].count('O') / 12) * 100,2)  for instance in checklist_need],
                width=[0.5]*len([val['room_num'] for val in checklist_need]),
                text =  [round(([val for val in instance.values()][27:39].count('O') / 12) * 100,2)  for instance in checklist_need],
                textposition='auto',
                
            )])
        fig1.update_layout(
        annotations=[dict(text='객실',font_size=20, showarrow=False)],
        yaxis=dict(
        title='환산 점수',
        titlefont_size=16,
        tickfont_size=14,
        ),
        xaxis=dict(
        title='호실번호',
        titlefont_size=16,
        tickfont_size=14,
        ))
        layout_bed = {
        'title': '객실항목',
        'height': 100,
        'width': 100,
        }
        fig1.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.0, opacity=0.6)
        
        fig_bed = plot({'data': fig1,'layout': layout_bed}, output_type='div')

        #욕실 바 그래프
        fig2 = go.Figure(data=[go.Bar(
                x = [val['room_num'] for val in checklist_need],
                y=[round(([val for val in instance.values()][39:].count('O')/17) * 100,2) for instance in checklist_need],
                width=[0.5] * len([val['room_num'] for val in checklist_need]),
                text =  [round(([val for val in instance.values()][39:].count('O') / 17) * 100,2)  for instance in checklist_need],
                textposition='auto',
                
            )])
        fig2.update_layout(
        annotations=[dict(text='욕실', font_size=20, showarrow=False)],
        yaxis=dict(
        title='환산 점수',
        titlefont_size=16,
        tickfont_size=14,
        ),
        xaxis=dict(
        title='호실번호',
        titlefont_size=16,
        tickfont_size=14,
        ))
        layout_bath = {
        'title': '욕실항목',
        'height': 100,
        'width': 100,
        }
        fig2.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.0, opacity=0.6)
        fig_bath = plot({'data': fig2,'layout': layout_bath}, output_type='div')

        context = {'fig_bed':fig_bed,
                    'fig_bath':fig_bath,
                    'checklist_need':checklist_need,
                    'label':label} 
    return render(request, 'report_division2.html',context)

def details(request):
    if request.user.is_authenticated:
        user = request.user
        lodge = lodges.objects.get(user_id= user.id)
        
        #사용해야하 checklist 인스턴스들 호출
        checklist_use = checklist.objects.filter(lodge_id = lodge.id).values().order_by('id').last()
        last_day = checklist_use['check_date']
        checklist_need = checklist.objects.filter(lodge_id = lodge.id)
        checklist_need = checklist_need.filter(check_date = last_day)
        rooms = [room['room_num'] for room in checklist_need.values() if len([val for val in room.values() if val == 'X']) > 0 ]
        checklist_need = checklist_need.filter(room_num__in = rooms).values()

        #방별 Key값 찾기 
        keys = [[int(key[1:]) for key in room.keys() if room[key] == 'X'] for room in checklist_need]

        #질문 찾기 
        questions = [[(feat.question_id, feat.question) for feat in features.objects.filter(question_id__in= key).all()] for key in keys]
        questions = list(zip(rooms, questions))
        rooms_cnt = len(questions)
        


        context = {'keys':keys,
                    'questions':questions,
                    'checklist_use':checklist_use.values(),
                    'rooms':rooms,
                    'checklist_need':checklist_need,
                    'rooms_cnt':rooms_cnt
                    }
    return render(request, 'report_details.html',context)