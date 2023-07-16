from django.core.files.storage import default_storage
from django.shortcuts import render
from django.core.paginator import Paginator 
from django.shortcuts import redirect
from .form import UploadExcelForm
from .models import Kit_data,\
                    Kit,\
                    Modulo,\
                    Inversor,\
                    Cabo,\
                    Pares,\
                    Stringbox,\
                    Estrutura
import openpyxl, pandas as pd
pd.set_option('display.max_columns', None)
# Create your views here.

def create_data (request):
    
    if request.method == 'POST':
        
        excel = request.FILES['file']
        data = pd.read_excel(excel)
        
        data_length = len(data)     
        column_names = list(data.columns.values)   
        #print(data_length, column_names)
        #input()
        print("\nprocesso de dados iniciado voce sera redirecionado a pagina de listagem ao termino")
        for row in range(data_length):
            
            salvar = Kit()
        
            salvar.identificacao_kit = data.loc[row]['Identificação Kit']
            salvar.codigo = data.loc[row]['Código']
            salvar.preco = data.loc[row]['Preço']
            salvar.telhado = data.loc[row]['Telhado']
            salvar.conexao = data.loc[row]['Conexão']

            salvar.save()

            search = Modulo.objects.filter(mod_modulo=data.loc[row]['Modelo Módulo'],
                                           qnt_modulos=data.loc[row]['Quant. Módulos']).values()
            #check Modulo
            if search:
                modulo = Modulo.objects.get(mod_modulo=data.loc[row]['Modelo Módulo'],
                                           qnt_modulos=data.loc[row]['Quant. Módulos'])

                salvar.modulos.add(modulo)
                #print('modulo existe')
            else :
                model_save = Modulo()

                model_save.mod_modulo =  data.loc[row]['Modelo Módulo']
                model_save.qnt_modulos = data.loc[row]['Quant. Módulos']
                model_save.marca_modulo = data.loc[row]['Marca do Módulo']
                model_save.potencia_unitaria = data.loc[row]['Potência Wp Unitária Módulo']
                model_save.max_overload = data.loc[row]['Overload Máximo']
                model_save.kwp = data.loc[row]['kWp']
                model_save.save()

                modulo = Modulo.objects.get(mod_modulo=data.loc[row]['Modelo Módulo'],
                                           qnt_modulos=data.loc[row]['Quant. Módulos'])  
                salvar.modulos.add(modulo)
                #print('modulo n existe e foi criado')

            #check Inversor
            check_inversor = Inversor.objects.filter(qnt_inversor = data.loc[row]['Qtde. Inversor 1'],
                                                  mod_inversor = data.loc[row]['Inversor 1']).values()

            if check_inversor:
                inversor = Inversor.objects.get(qnt_inversor = data.loc[row]['Qtde. Inversor 1'],
                                                  mod_inversor = data.loc[row]['Inversor 1'])

                salvar.inversor.add(inversor)
                #input('existe inverso')

            else:
                model_save = Inversor()

                model_save.qnt_inversor = data.loc[row]['Qtde. Inversor 1']
                model_save.mod_inversor = data.loc[row]['Inversor 1']
                model_save.marca_inversor =  data.loc[row]['Marca do Inversor']
                model_save.save()

                inversor = Inversor.objects.get(qnt_inversor = data.loc[row]['Qtde. Inversor 1'],
                                                  mod_inversor = data.loc[row]['Inversor 1'])

                salvar.inversor.add(inversor)
                #input('inversor n existe criado com sucesso')

            #check cabo 1
            check_cabo = Cabo.objects.filter(qnt_cabo = data.loc[row]['Quant. Cabo Vermelho (m)'],
                                             modelo = data.loc[row]['Modelo Cabo Vermelho'])

            if check_cabo:
                cabo = Cabo.objects.get(qnt_cabo = data.loc[row]['Quant. Cabo Vermelho (m)'],
                                             modelo = data.loc[row]['Modelo Cabo Vermelho'])
                salvar.cabo.add(cabo)
                #print('cabo existe no sistema')
            else:

                model_save = Cabo()

                model_save.modelo = data.loc[row]['Modelo Cabo Vermelho']
                model_save.qnt_cabo = data.loc[row]['Quant. Cabo Vermelho (m)']
                model_save.save()

                cabo = Cabo.objects.get(qnt_cabo = data.loc[row]['Quant. Cabo Vermelho (m)'],
                                             modelo = data.loc[row]['Modelo Cabo Vermelho'])
                salvar.cabo.add(cabo)
                #input('cabo nao existe e foi criado')

            #check cabo 2
            check_cabo = Cabo.objects.filter(qnt_cabo = data.loc[row]['Quant. Cabo Preto (m)'],
                                             modelo = data.loc[row]['Modelo Cabo Preto'])

            if check_cabo:
                cabo = Cabo.objects.get(qnt_cabo = data.loc[row]['Quant. Cabo Preto (m)'],
                                             modelo = data.loc[row]['Modelo Cabo Preto'])
                salvar.cabo.add(cabo)
                #print('cabo 2 existe no sistema')
            else:

                model_save = Cabo()

                model_save.modelo = data.loc[row]['Modelo Cabo Preto']
                model_save.qnt_cabo = data.loc[row]['Quant. Cabo Preto (m)']

                model_save.save()

                cabo = Cabo.objects.get(qnt_cabo = data.loc[row]['Quant. Cabo Preto (m)'],
                                             modelo = data.loc[row]['Modelo Cabo Preto'])
                salvar.cabo.add(cabo)
                #input('cabo 2 nao existe e foi criado')

            #check pares
            check_pares = Pares.objects.filter(qnt_pares_conectores = data.loc[row]['Quant. Pares Conectores'],
                                             mod_par_conector = data.loc[row]['Modelo Par Conector'])
            if check_pares:
                par = Pares.objects.get(qnt_pares_conectores = data.loc[row]['Quant. Pares Conectores'],
                                             mod_par_conector = data.loc[row]['Modelo Par Conector'])
                salvar.pares.add(par)
                #print('pares existe')
            else:
            
                model_save = Pares()

                model_save.qnt_pares_conectores = data.loc[row]['Quant. Pares Conectores']
                model_save.mod_par_conector = data.loc[row]['Modelo Par Conector']
                model_save.save()

                par = Pares.objects.get(qnt_pares_conectores = data.loc[row]['Quant. Pares Conectores'],
                                             mod_par_conector = data.loc[row]['Modelo Par Conector'])
                salvar.pares.add(par)
                #print('pares n existe e foi criado existe')

            #check Stringbox
            exist = data.loc[row]['Quant. Stringbox']

            if pd.isna(exist) == False:
                
                check_string_box  = Stringbox.objects.filter(qnt_stringbox = data.loc[row]['Quant. Stringbox'],
                                             mod_stringbox = data.loc[row]['Modelo Stringbox'])
            
                if check_string_box:
                    stringbox = Stringbox.objects.get(qnt_stringbox = data.loc[row]['Quant. Stringbox'],
                                                 mod_stringbox = data.loc[row]['Modelo Stringbox'])
                    salvar.stringbox.add(stringbox)
                    #print("stringbox existed")

                else:

                    model_save = Stringbox()

                    model_save.qnt_stringbox = data.loc[row]['Quant. Stringbox']
                    model_save.mod_stringbox = data.loc[row]['Modelo Stringbox']
                    model_save.save()

                    stringbox = Stringbox.objects.get(qnt_stringbox = data.loc[row]['Quant. Stringbox'],
                                                 mod_stringbox = data.loc[row]['Modelo Stringbox'])
                    salvar.stringbox.add(stringbox)
            
            #check estrutura
            
            qnt_estrutura = ['Quant. Estrutura 1',
                             'Quant. Estrutura 2',
                             'Quant. Estrutura 3',
                             'Quant. Estrutura 4',
                             'Quant. Estrutura 5']
            
            mod_estrutura = ['Modelo Estrutura 1',
                             'Modelo Estrutura 2',
                             'Modelo Estrutura 3',
                             'Modelo Estrutura 4',
                             'Modelo Estrutura 5']
            
            for estrutura, modelo in zip(qnt_estrutura, mod_estrutura):
            
                if pd.isna(data.loc[row][estrutura]) == False:

                    check_estrutura = Estrutura.objects.filter(qnt_estrutura1 = data.loc[row][estrutura],
                                                     mod_estrutura1 = data.loc[row][modelo])

                    if check_estrutura:

                        estrutura = Estrutura.objects.get(qnt_estrutura1 = data.loc[row][estrutura],
                                                          mod_estrutura1 = data.loc[row][modelo])
                        salvar.estrutura.add(estrutura)

                    else:
                        model_save = Estrutura()

                        model_save.qnt_estrutura1 = data.loc[row][estrutura]
                        model_save.mod_estrutura1 = data.loc[row][modelo]
                        model_save.save()

                        estrutura = Estrutura.objects.get(qnt_estrutura1 = data.loc[row][estrutura],
                                                          mod_estrutura1 = data.loc[row][modelo])
                        salvar.estrutura.add(estrutura)
        
        return redirect(listagem)               
            
                               
    else:
        form = UploadExcelForm()

    return render (request, 'sender.html', {'form': form})

def listagem (request):
    
    kits =  Kit.objects.all()
    
    kit_paginator = Paginator(kits, len(kits))
    page_num = request.GET.get('page')
    page = kit_paginator.get_page(page_num)
    
    return render (request, 'home.html', {'page': page})
def excel (request):
    
    if request.method == 'POST':
        
        salvar = Kit_data()
        
        data = UploadExcelForm(request.POST, request.FILES)
        excel = request.FILES['file']
        x = pd.read_excel(excel)
        x.fillna(0)
        lista = x.columns.values
        print(lista)
        
        print(x.loc[0]['Código'])
        
        
        salvar.identificacao_kit = x.loc[0]['Identificação Kit']
        salvar.codigo = x.loc[0]['Código']
        salvar.preco = x.loc[0]['Preço']
        salvar.telhado = x.loc[0]['Telhado']
        salvar.conexao = x.loc[0]['Conexão']
        salvar.qnt_modulos = x.loc[0]['Quant. Módulos']

        salvar.mod_modulo = x.loc[0]['Modelo Módulo']
        salvar.potencia_unitaria = x.loc[0]['Potência Wp Unitária Módulo']
        salvar.max_overload = x.loc[0]['Overload Máximo']
        salvar.kwp = x.loc[0]['kWp']

        salvar.qnt_inversor1 = x.loc[0]['Qtde. Inversor 1']
        salvar.invesor1 = x.loc[0]['Inversor 1']
        salvar.qnt_inversor2 = x.fillna(0).loc[0]['Qtde. Inversor 2']
        salvar.invesor2 = x.fillna(0).loc[0]['Inversor 2']

        salvar.qnt_cabo_vermelho_m = x.loc[0]['Quant. Cabo Vermelho (m)']
        salvar.mod_cabo_vermelho = x.loc[0]['Modelo Cabo Vermelho']
        salvar.qnt_cabo_preto_m = x.loc[0]['Quant. Cabo Preto (m)']
        salvar.mod_cabo_preto = x.loc[0]['Modelo Cabo Preto']

        salvar.qnt_pares_conectores = x.loc[0]['Quant. Pares Conectores']
        salvar.mod_par_conector = x.loc[0]['Modelo Par Conector']
        salvar.qnt_stringbox = x.loc[0]['Quant. Stringbox']
        salvar.mod_stringbox = x.loc[0]['Modelo Stringbox']

        salvar.qnt_estrutura1 = x.loc[0]['Quant. Estrutura 1']
        salvar.mod_estrutura1 = x.loc[0]['Modelo Estrutura 1']
        salvar.qnt_estrutura2 = x.fillna(0).loc[0]['Quant. Estrutura 2']
        salvar.mod_estrutura2 = x.fillna(0).loc[0]['Modelo Estrutura 2']
        salvar.qnt_estrutura3 = x.fillna(0).loc[0]['Quant. Estrutura 3']
        salvar.mod_estrutura3 = x.fillna(0).loc[0]['Modelo Estrutura 3']
        salvar.qnt_estrutura4 = x.fillna(0).loc[0]['Quant. Estrutura 4']
        salvar.mod_estrutura4 = x.fillna(0).loc[0]['Modelo Estrutura 4']
        salvar.qnt_estrutura5 = x.fillna(0).loc[0]['Quant. Estrutura 5']
        salvar.mod_estrutura5 = x.fillna(0).loc[0]['Modelo Estrutura 5']

        salvar.marca_inversor = x.loc[0]['Marca do Inversor']
        salvar.mod_modulo = x.loc[0]['Marca do Módulo']
        
        salvar.save()
        
 
        input('\n>>> okay >>>')
    else:
        form = UploadExcelForm()

    return render (request, 'sender.html', {'form': form})