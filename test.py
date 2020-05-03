from appJar import gui
import postgresql
import matplotlib.pyplot as plt
from numpy import sin, pi, arange
from appJar import gui
import random


def connect_to_db():
    db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
    con_db = postgresql.open(db)
    return con_db


def download_table_names_list():
    con_db = connect_to_db()
    table_list = con_db.prepare("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public'")
    table_names_list = []
    for table_name in table_list:
        if type(table_name) is not type(None):
            mes = str(table_name)
            mes1 = mes.replace('(', '')
            mes2 = mes1.replace(')', '')
            mes3 = mes2.replace('\'', '')
            mes4 = mes3[:-1]
        table_names_list.append(mes4)
        table_names_list.sort()
        # print(table_names_list)
    return table_names_list


def download_column_names_list(btn):
    con_db = connect_to_db()
    table_names_list = download_table_names_list()
    list_for_optionbox = []
    # list_for_def = []
    for table_name in table_names_list:
        column_list = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + str(table_name) + '\''
        column_list = con_db.prepare(column_list)
        bes = ''
        for i in column_list:
            bes += str(i)
            bes1 = bes.replace('(', '')
            bes2 = bes1.replace(')', '')
            bes3 = bes2.replace('\'', '')
            bes4 = bes3[:-1]
            bes5 = '{} | {}'.format(bes4,table_name)
            # bes6 = '{},{}'.format(bes4,table_name)
            # print('bes5','',bes5)
            # list_for_def.append(bes6)
            list_for_optionbox.append(bes5)
        # print('list1', '', list)

    # print('list2', '', list)
    column_names_list = []
    for i in list_for_optionbox:
        if i.count(',') > 0:
            i = i.split(',')
            column_names_list.append(i[-1])
        else:
            column_names_list.append(i)
    # print(column_names_list)
    if btn == 'download_column_names_list':
        app.changeOptionBox('column_names', column_names_list)
    # print(list_for_def)
    # return list_for_def




def download_column_names_info():
    con_db = connect_to_db()
    column_names = app.getOptionBox('column_names')
    # print(column_names)
    true_column_list = []
    for key,value in column_names.items():
        if value == True:
            true_column_list.append(key)
    # print(true_column_list)
    list_for_download = []
    # list_of_columns = []
    # list_of_tables = []
    for i in true_column_list:
        # if i.count('') > 0:
        i = i.split(' | ')
        list_for_download.append(i)
        # print(list_for_download)
    info_for_graf = {}
    for name in list_for_download:
        # print(name)
        list_name = name[0]
        table_name = name[1]
        sql_code = 'select' + ' ' + list_name + ' ' + 'from' + ' ' + table_name
        info = con_db.prepare(sql_code)
        nes = ''
        for i in info:
            nes = nes + str(i)
            nes1 = nes.replace('(', '')
            nes2 = nes1.replace(')', '')
            nes3 = nes2.replace('\'', '')
            nes4 = nes3.replace('Decimal', '')
            nes5 = nes4[:-1]
            nes6 = nes5.split(',')
            numbers = []
            for n in nes6:
                if n != 'None':
                   nes7 = int(n)
                   numbers.append(nes7)

        # print(l)
        graf_name =  '{} | {}'.format(list_name,table_name)
        # print(graf_name,numbers)

        info_for_graf[graf_name]=numbers
        # print(info_for_graf)
    return info_for_graf
        # return graf_name,numbers
        # return graf_name,numbers

        # list_of_columns.append(list_name)
        # list_of_tables.append(table_name)
    # print(true_column_list)
    # print(list_for_download)
    # print(list_of_columns)
    # print(list_of_tables)
    # for table_name in table_list:
    #     for column_name in :
    #         if column_name.values() == True:
    #             data = con_db.prepare('SELECT' + column_name + ' ' + 'FROM' + str(table_name))
#
# def show():
#     column_list = app.changeOptionBox('table_names', column_list)
#     a1 = 'download_column_names_infoect' + ' ' + str(app.getOptionBox('Поле таблицы оси X')) + ' ' + 'from' + ' ' + str(
#         app.getOptionBox('Таблица Оси X'))
#     table1Info = con_db.prepare(a1)
# def showLabels():
#     ax.legend()
#     ax.set_xlabel('Поле таблицы оси X')
#     ax.set_ylabel('Ось Y')
#     app.refreshPlot('p1')
def subWindGrafik(btn):
    global l
    # if str(app.getOptionBox('Тип графика')) == 'График':
    # if btn == 'download_column_names_info':
    info = download_column_names_info()
    x = [1,2,3,4,5,6,7]

    l = []
        # i=0
        # for n in l:
        #     if n != n[i+1] or n == n:


    for name,value in info.items():
        a = plt.plot(x, value,label=name)
        # a = ax.plot(x, value, label=name)
        plt.xlabel('x_value')
        plt.title('Histogram of IQ')
        plt.grid(True)
        plt.legend()
        l.append(a)


    # elif btn == 'close':
    #     l = []

        # fig, ax = plt.subplots()
        # a = ax.plot(x, value)
        #
        # ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        #        title='About as simple as it gets, folks')
        # ax.grid()

        # fig.savefig("test.png")
        # print(type(a))
    # return


    # list_of_values = info.values()
    # i = 0
    # print(list_of_values)
    # i += 1
    # app.refreshPlot('p1')
    # ax.plot(x, value)
    # app.updatePlot('p1',)
    # showLabels()
    # ax.plot(x, value, label=name)
    # ax.set_xlabel(app.getOptionBox('Поле таблицы оси X'))
    # ax.set_ylabel('Ось Y')
    # app.refreshPlot('p1')
    # app.getN
    # ax.legend()
    # plt.show()
    # ax.plot(x, value, label=name)
    # ax.set_xlabel('Поле таблицы оси X')
    # ax.set_ylabel('Ось Y')

    # plt.show()
    # app.showSubWindow('grafik')
    # i += 1
    # print(i)
    # for k in list_of_values:
    # if len(list_of_values[0] == len(list_of_values[i])):
    # print(k)
    # print(name)
    # i += 1
    # ax.plot(x, k, label=name)
    # ax.set_xlabel('Поле таблицы оси X')
    # ax.set_ylabel('Ось Y')
    # ax.legend()
    # plt.show()
    # app.showSubWindow('grafik')
    # else:
    #     app.infoBox('Ошибка', 'Ошибка размерности')

def getXY():
    x = arange(0.0, 3.0, 0.01)
    y = sin(random.randint(1,10) * pi * x)
    return x,y


def push(btn):
    global l
    if btn == 'download_column_names_list':
        app.showSubWindow('choice')
        download_column_names_list(btn)
    elif btn == 'download_column_names_info':
        subWindGrafik(btn)# subWindGrafik()
        # ax.legend()

        # app.refreshPlot('p1')
        # plt.show()
        plt.savefig("test.png")
        app.reloadImage("grafik", "test.png")
        app.showSubWindow('grafik')

        # plt.show()
        # plt.savefig("test.png")
        # plt.show(subWindGrafik())

    elif btn == 'close':
        # app.updatePlot('p1',[0],[0])
        # app.refreshPlot('p1')
        # app.emptyPlot('p1')
        # app.removePlot('p1')
        # app.removeCanvas('p1')
        # app.emptyCurrentContainer()
        # subWindGrafik(btn)
        # app.emptyCurrentContainer()
        plt.cla()
        plt.clf()
        plt.close()
        app.hideSubWindow('grafik')
        # del l


app = gui('Программа')
app.addButton('download_column_names_list', push)

app.startSubWindow('grafik')
# fig = app.addPlotFig('p1')
# ax = fig.subplots()
app.addImage("grafik", "test.png")
app.addButton('close',push)
app.stopSubWindow()

app.startSubWindow('choice', 'choice')

app.addTickOptionBox('column_names', ['Данные не загрузились'])
app.addButton('download_column_names_info', push)
app.stopSubWindow()

app.go()
# print(download_column_names_info())






















