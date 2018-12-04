from errbot import BotPlugin, botcmd, re_botcmd

class buzau(BotPlugin):
    """O Juaum que almentu"""    



    @botcmd
    def start(self, msg, args):
        """Inicio do bot"""
        yield "Ola, digite o nome da linha que deseja ou se preferir consulte as /empresas."
    
#-------------------------------------------------------------------------------    
    @re_botcmd(pattern=r"^[Ee]mpresa.*$")
    def empresas(self, msg, args):
        """Consulta de empresas"""
        yield """As empresas sao:
/biguacu

/estrela

/imperatriz

/jotur

/santa_terezinha"""
    
    @re_botcmd(pattern=r"^[Bb]igua.*$")
    def biguacu(self, msg, args):
        yield """Por favor, selecione a linha que deseja:
/Tres_Riachos
/Tres_Riachos_Viaduto_Janaina
/Tijucas
/Sorocaba
/Sorocaba_Viaduto_Janaina
/Shopping_Center_Itaguacu
/Serraria_Forquilhinha
/Saudade
/Sao_Miguel
/Santa_Maria_Antonio_Carlos
/Bom_Viver
/Circular_Barreiros
/Diretao
OBS:. As outras linhas serao adicionadas posteriormente"""
    @re_botcmd(pattern=r"^[Ee]stre.*$")
    def estrela(self, msg, args):
        """Vamos ver se da"""
        yield """Escolha o que deseja na proxima mensagem 
/EstrelaInterMunicipal
/EstrelaMunicipal"""

        msg.ctx['xx1'] = 'Escolha entre as linhas Municipais'
        msg.ctx['yy1'] = 'Escolha entre as linhas intermunicipais'

    @botcmd
    def EstrelaInterMunicipal(self, msg, args, flow_only=True):
        """InterMunicipais"""
        try:
            yield msg.ctx['yy1'] + """
/CH_Arthur_Mariano_Circular_Forquilhinha
/CH_Forquilhinha
/Campinas
/Campinas_Via_Ginasio_de_Esportes
/CEASA_Via_Santos_Saraiva
/Ceniro_Via_Jardim_das_Palmeiras
/D_Zenaide_Via_Santa_Feliciadade_Ceniro
/EXECUTIVO_San_Marino_Lisboa
/Forquilhas_Florianopolis
/Forquilhinha_Via_Rodeio_e_Palmares
/Kobrasol
/Kobrasol_VIP
/Los_Angeles
/Parque_Residencial_Lisboa
/Potecas
/Potecas_Santos_Saraiva
/Recanto_da_Natureza_Via_Ceniro_Martins
/Sao_Luiz
"""
        except:
            yield 'tente novamente'

    @botcmd
    def EstrelaMunicipal(self, msg, args, flow_only=True):
        """Municipais"""
        try:
            yield  """
/Serraria_Forquilhinha
/Barreiros_Sede
/Forquilhas_Kobrasol
/Vila_Formosa_Lisboa_Kobrasol
/Diretao
/Potecas_Kobrasol
/Executivo_Diretao"""
        except:
            yield "Primeiro informe a linha que deseja"

    @re_botcmd(pattern=r"^[Ii]mperatri.*$")
    def imperatriz(self, msg, args):
        yield """
/Alto_Aririu_Florianopolis
/Capela_Alto_Aririu_Florianopolis
/Aririu_Caldas_Imperatriz
/Aguas_Mornas_Florianopolis
/Capela_Alto_Aririu_Florianopolis_Rod_Municipais
/Florianopolis_Caldas_da_Imperatriz
/Florianopolis_Caldas_da_Imperatriz_SF_BR
/Lourdes2_Florianopolis
/Lourdes2_SA_Imperatriz
/Quecaba
/SA_Imperatriz_Florianopolis670
/SA_Imperatriz_Florianopolis6271
/SA_Imperatriz_Florianopolis6270
/SA_Imperatriz_Florianopolis6261
/SA_Imperatriz_Florianopolis6260
/SA_Imperatriz_Florianopolis671
/Santa_Isabel_Florianopolis
/Vargem_Grande_2_Florianopolis"""

    @re_botcmd(pattern=r"^[Jj]otu.*$")
    def jotur(self, msg, args):
        yield """
/Bairro_Sao_Luiz143
/Forquilhas08
/Irineu_Comelli
/Hospital_Regional
/Ponta_de_Baixo
OBS:. As outras linhas serao adicionadas posteriormente"""

    @re_botcmd(pattern=r"^[Ss]anta.*[Tt]ere.*")
    def santa_terezinha(self, msg, args):
        yield """Por favor, selecione a linha que deseja:
/Jardim_Pinheiros_Kobrasol

/Continente_Park_Shopping_Florianopolis

/Flor_de_Napolis_Santo_Andre

/Santana_Florianopolis

/Santana_Kobrasol

/Sao_Pedro_de_Alcantra_Florianopolis

/Coqueiros_Angelina_Betania_e_Rancho_Queimado

/Sertao_do_Maruim_Florianopolis

/Vila_Formosa_Florianopolis"""

    @botcmd
    def sta_terezinha(self, msg, args):
        yield """Por favor, selecione a linha que deseja:
/Jardim_Pinheiros_Kobrasol

/Continente_Park_Shopping_Florianopolis

/Flor_de_Napolis_Santo_Andre

/Santana_Florianopolis

/Santana_Kobrasol

/Sao_Pedro_de_Alcantra_Florianopolis

/Coqueiros_Angelina_Betania_e_Rancho_Queimado

/Sertao_do_Maruim_Florianopolis

/Vila_Formosa_Florianopolis"""
#----------------------------------------------------------------------------------------------------------------------------------------------------

    @re_botcmd(pattern=r"^[Jj]ardim.*[Pp]inheiro.*$")
    def Jardim_Pinheiros_Kobrasol(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Jardim_Pinheiros_Kobrasol

/rota_Jardim_Pinheiros_Kobrasol"""

    @botcmd
    def horario_Jardim_Pinheiros_Kobrasol(self, msg, args, flow_only=True):
        """Jardim Pinheiros Kobrasol"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta0900
/SaidasCentroSegundaaSexta0900
/SaidasBairroSabadosDomingoseFeriados0900
/SaidasCentroSabadosDomingoseFeriados0900"""
        msg.ctx['x1'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y1'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z1'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w1'] = 'Saidas do centro de sabados, domingos e feriados:'
        

    @botcmd
    def SaidasBairroSegundaaSexta0900(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""

        try:
            yield msg.ctx['x1'] + """
|07:00|
|08:00|
|09:00|
|12:50|
|15:00|
|18:20|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta0900(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y1'] + """
|07:30|
|08:30|
|11:55|
|13:10|
|17:45|
|19:10|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados0900(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z1'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados0900(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w1'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Usar 58 yy para copiar da linha de baixo dessa
#    @botcmd
#    def linha_do_onibus(self, msg, args):
#        yield """Ola, o que deseja saber?
#/horario_linha_do_onibus
#
#/rota_linha_do_onibus"""
#
#    @botcmd
#    def horario_linha_do_onibus(self, msg, args):
#        """Linha do Onibus"""
#        yield """Qual saida?
#/SaidasBairroSegundaaSexta
#/SaidasCentroSegundaaSexta
#/SaidasBairroSabadosDomingoseFeriados
#/SaidasCentroSabadosDomingoseFeriados"""
#        msg.ctx['x.'] = 'Saidas do bairro de segunda a sexta:'
#        msg.ctx['y.'] = 'Saidas do centro de segunda a sexta:'
#        msg.ctx['z.'] = 'Saidas do bairro de sabados, domingos e feriados:'
#        msg.ctx['w.'] = 'Saidas do centro de sabados, domingos e feriados:'
#
#    @botcmd
#    def SaidasBairroSegundaaSexta(self, msg, args, flow_only=True):
#        """Saidas do bairro de segunda a sexta"""
#        try:
#            yield msg.ctx['x.'] + """horario"""
#        except:
#            yield "Primeiro informe a linha que deseja"
#
#    @botcmd
#    def SaidasCentroSegundaaSexta(self, msg, args, flow_only=True):
#        """Saidas do centro de segunda a sexta"""
#        try:
#            yield msg.ctx['y.'] + """horario"""
#        except:
#            yield "Primeiro informe a linha que deseja"
#
#    @botcmd
#    def SaidasBairroSabadosDomingoseFeriados(self, msg, args, flow_only=True):
#        """Saidas do bairro de sabados, domingos e feriados"""
#        try:
#            yield msg.ctx['z.'] + """
#Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
#-> /empresas"""
#        except:
#            yield "Primeiro informe a linha que deseja"
#
#    @botcmd
#    def SaidasCentroSabadosDomingoseFeriados(self, msg, args, flow_only=True):
#        """Saidas do centro de sabados, domingos e feriados"""
#        try:
#            yield msg.ctx['w.'] + """
#Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
#-> /empresas"""
#        except:
#            yield "Primeiro informe a linha que deseja"
#
#
#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[Cc]ontinente.*[Ss]ho.*$")
    def Continente_Park_Shopping_Florianopolis(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Continente_Park_Shopping_Florianopolis

/rota_Continente_Park_Shopping_Florianopolis"""

    @botcmd
    def horario_Continente_Park_Shopping_Florianopolis(self, msg, args):
        """Continente Park Shopping Florianopolis"""
        yield """Qual saida?
/SaidasBairroSegundaaSextaSN
/SaidasCentroSegundaaSextaSN
/SaidasBairroSabadosDomingoseFeriadosSN
/SaidasCentroSabadosDomingoseFeriadosSN"""
        msg.ctx['x2'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y2'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z2'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w2'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSextaSN(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x2'] + """
|07:00|D
|07:40|D
|08:15|
|08:55|D
|09:10|
|10:40|D
|12:05|D
|13:10|EXP
|13:25|D
|13:55|D
|16:15|
|16:35|
|17:10|
|17:25|D
|17:50|D
|18:10|
|19:05|
|19:40|D
|20:55|D
|21:25|
|22:08|
|22:29|
|22:40|D
-
EXP: Via Expressa
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSextaSN(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y2'] + """
|06:30|D
|07:35|
|07:50|EXP D
|08:20|
|09:05|D
|09:30|
|09:50|D
|10:30|D
|11:15|D
|11:35|D
|12:10|D
|12:57|D
|13:43|
|14:15|
|14:55|D
|15:30|
|16:12|
|16:30|D
|17:00|
|17:25|
|17:45|D
|18:04|
|19:00|
|19:18|D
|21:25|
|22:05|D
|23:00|D
-
EXP: Via Expressa
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriadosSN(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z2'] + """
Sabados:
|07:05|D
|08:20|D
|08:40|D
|10:05|D
|10:30|D
|11:15|D
|12:25|D
|13:40|D
|14:20|D
|16:20|D
|17:00|D
|17:55|D
|18:25|D
|19:15|D
|20:10|D
|22:20|D
-
Domingos e feriados:
|07:00|D
|08:00|D
|11:05|D
|11:40|D
|13:10|D
|15:40|D
|16:35|D
|16:55|D
|17:50|D
|18:25|D
|19:15|D
|20:10|D
|21:00|D
|22:20|D
-
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriadosSN(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w2'] + """
Sabados:
|07:30|D
|08:30|
|09:15|D
|10:15|D
|11:20|D
|12:05|
|13:15|D
|14:30|D
|16:05|D
|17:40|D
|19:20|D
|20:35|D
|21:30|D
|22:30|D
-
Domingos e feriados:
|07:10|D
|09:45|D
|12:00|D
|14:30|D
|15:50|D
|06:30|D
|17:40|D
|19:20|D
|20:35|D
|21:40|D
-
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Coqueiros_Angelina_Betania_e_Rancho_Queimado(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Coqueiros_Angelina_Betania_e_Rancho_Queimado

/rota_Coqueiros_Angelina_Betania_e_Rancho_Queimado"""

    @botcmd
    def horario_Coqueiros_Angelina_Betania_e_Rancho_Queimado(self, msg, args):
        """Coqueiros Angelina Betania e Rancho Queimado"""
        yield """qual saida?
/SaidasBairroSegundaaSexta553
/SaidasCentroSegundaaSexta553
/SaidasBairroSabadosDomingoseFeriados553
/SaidasCentroSabadosDomingoseFeriados553"""
        msg.ctx['x3'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y3'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z3'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w3'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta553(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x3'] + """
Horario de segunda:
|05:00| Coqueiros Via Rancho Queimado
|06:00| Rancho Queimado
|06:15| Barro Branco
-
Horario de terca a quinta:
|05:30| Coqueiros Via Sao Pedro
|05:30| Angelina Via Rancho Queimado
-
Horario de sexta:
|05:30| Coqueiros Via Sao Pedro
|05:30| Angelina Via Rancho Queimado"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSegundaaSexta553(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y3'] + """
Horario de segunda:
|13:10| Coqueiros Via Sao Pedro de Alcantara
|17:25| Angelina Via Rancho Queimado ate Hospital Angelina
-
Horario de terca a quinta:
|13:10| Coqueiros Via Sao Pedro
|17:25| Angelina Via Rancho Queimado ate Hospital Angelina
-
Horario de sexta:
|13:10| Coqueiros Via Sao Pedro
|16:15| Betania Via Sao Pedro
|17:10| Coqueiros Via Rancho Queimado"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados553(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z3'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados553(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w3'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[FfGgDd]lor.*[NnMmBb]apolis.*$")
    def Flor_de_Napolis_Santo_Andre(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Flor_de_Napolis_Santo_Andre

/rota_Flor_de_Napolis_Santo_Andre"""

    @botcmd
    def horario_Flor_de_Napolis_Santo_Andre(self, msg, args):
        """Flor de Napolis Santo Andre"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta175
/SaidasCentroSegundaaSexta175
/SaidasBairroSabadosDomingoseFeriados175
/SaidasCentroSabadosDomingoseFeriados175"""
        msg.ctx['x4'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y4'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z4'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w4'] = 'Saidas do centro de sabados, domingos e feriados:'
        

    @botcmd
    def SaidasBairroSegundaaSexta175(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x4'] + """
|05:35| SA
|06:00| SA
|06:20| SA
|06:35| SA EXP BR
|06:50| SA
|07:03| SA
|07:25| SA
|07:50| SA
|08:10| SA
|08:30| SA
|09:10| SA
|10:00| SA
|10:55| SA
|13:00| SA
|14:10| SA
|15:00| SA
|16:00| SA
|16:40| SA
|17:15| SA
|17:40| SA
|18:10| SA
|18:30| SA
|19:20| SA
|20:05| SA
|21:00| SA
|22:00| SA
|23:00| SA
-
SA: Via Rua Santo Andre
EXP: Via Expressa
BR: Via BR 101"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta175(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y4'] + """
|06:00| FN
|06:30| SA
|07:20| EXP FN
|07:40| FN EXP BR
|08:00| SA
|08:40| SA
|09:20| SA
|10:20| SA
|11:00| SA
|11:25| SA
|11:55| SA
|12:30| SA
|13:00| SA
|13:40| SA
|14:10| SA
|14:58| SA
|15:40| SA
|16:15| SA
|16:45| SA
|17:15| SA
|17:44| SA
|18:20| SA
|18:50| SA
|19:20| SA
|19:55| SA
|21:00| SA
|22:00| SA
|22:30| SA
|23:45| SA
-
SA: Via Rua Santo Andre
EXP: Via Expressa
BR: Via BR 101
FN: Rua 25 de Dezembro"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados175(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z4'] + """
Sabados:
|06:00| SA
|06:30| SA
|07:00| SA
|07:30| SA
|08:00| SA
|08:35| SA
|09:10| SA
|10:00| SA
|11:00| SA
|12:00| SA
|13:00| SA
|14:10| SA
|15:20| SA
|16:30| SA
|17:30| SA
|18:10| SA
|19:30| SA
|21:00| SA
|23:15| SA
-
Domingos e feriados:
|06:00| SA
|07:10| SA
|09:00| SA
|11:00| SA
|12:20| SA
|13:40| SA
|15:00| SA
|16:30| SA
|18:10| SA
|19:30| SA
|21:00| SA
|23:15| SA
-
SA: Via Rua Santo Andre"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados175(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w4'] + """
Sabados:
|06:30| SA
|07:00| SA
|07:30| SA
|08:10| SA
|08:40| SA
|09:20| SA
|10:10| SA
|11:00| SA
|11:50| SA
|12:40| SA
|13:30| SA
|14:40| SA
|16:00| SA
|17:00| SA
|18:00| SA
|19:00| SA
|20:20| SA
|22:00| SA
|23:45| SA
-
Domingos e feriados:
|06:30| SA
|08:20| SA
|10:00| SA
|11:30| SA
|13:10| SA
|14:20| SA
|15:35| SA
|17:10| SA
|19:00| SA
|20:20| SA
|22:00| SA
|23:45| SA
-
SA: Via Rua Santo Andre"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[SsAaDd]antan.*[FfdDGg]lorianopol.*")
    def Santana_Florianopolis(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Santana_Florianopolis

/rota_Santana_Florianopolis"""

    @botcmd
    def horario_Santana_Florianopolis(self, msg, args):
        """Santana Florianopolis"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta178
/SaidasCentroSegundaaSexta178
/SaidasBairroSabadosDomingoseFeriados178
/SaidasCentroSabadosDomingoseFeriados178"""
        msg.ctx['x5'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y5'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z5'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w5'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta178(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x5'] + """
|05:00| A
|05:55| 
|06:25|
|07:05|
|07:30|
|09:00|
|09:30|
|10:30|
|11:20| D
|11:45|
|12:30|
|12:50| EXP SC
|13:45|
|14:55| SC
|16:00| D
|17:00| A
|18:00| EXP
|19:00| D
|20:15|
-
EXP: Via Expressa
A: Via Aeroclube
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta178(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y5'] + """
|05:45|
|06:42|
|07:40|
|08:35|
|09:30| SC
|10:30| SC D
|11:30| D
|12:45|
|13:43| SC
|15:00| D
|15:55|
|16:55| A
|17:25| SC
|17:45| D SC
|18:04| SC
|19:00| SC
|19:38|
|21:45| A
|22:30| A
-
A: Via Aeroclube
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados178(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z5'] + """
Sabados:
|06:00| A D
|06:45| 
|07:30| D
|08:30| A D
|09:30|
|10:30| A D
|11:00| SC D
|12:45| D
|15:20| A D
|17:10| D
|19:00| SC D
-
Domingos e feriados:
|10:50| SC D
|15:00| D
|17:10| D
|19:00| SC D
-
A: Via Aeroclube
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados178(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w5'] + """
Sabados:
|06:50| D
|07:30| SC D
|08:30| SC
|09:00| D
|10:15| SC D
|11:30| D
|14:30| A SC D
|16:24| D
|18:00| D
|20:50| D
-
Domingos e feriados:
|09:00| D
|16:30| D SC
|18:00| D
|20:50| D
-
A: Via Aeroclube
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[SsaADd]antana.*[KklLJj]obras.*$")
    def Santana_Kobrasol(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Santana_Kobrasol

/rota_Santana_Kobrasol"""

    @botcmd
    def horario_Santana_Kobrasol(self, msg, args):
        """Santana Kobrasol"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta901
/SaidasCentroSegundaaSexta901
/SaidasBairroSabadosDomingoseFeriados901
/SaidasCentroSabadosDomingoseFeriados901"""
        msg.ctx['x6'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y6'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z6'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w6'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta901(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x6'] + """
|06:40| A
|12:40|
-
A: Via Aeroclube"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta901(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y6'] + """
|11:55| A
|17:50| A
-
A: Via Aeroclube"""
        except:
            yield msg.ctx['x6'] + "Primeiro informe a linha que deseja"
            
    @botcmd
    def SaidasBairroSabadosDomingoseFeriados901(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z6'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados901(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w6'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[SsDdAa]ao.*[PpOo]edro.*[AaSs]lcan.*$")
    def Sao_Pedro_de_Alcantra_Florianopolis(self, msg, args):
       yield """Ola, o que deseja saber?
/horario_Sao_Pedro_de_Alcantra_Florianopolis

/rota_Sao_Pedro_de_Alcantra_Florianopolis"""

    @botcmd
    def horario_Sao_Pedro_de_Alcantra_Florianopolis(self, msg, args):
        """Sao Pedro de Alcantra Florianopolis"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta177
/SaidasCentroSegundaaSexta177
/SaidasBairroSabadosDomingoseFeriados177
/SaidasCentroSabadosDomingoseFeriados177"""
        msg.ctx['x7'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y7'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z7'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w7'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta177(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x7'] + """
|05:00| D
|05:30| LV
|06:00| D
|06:00| D
|06:20| D LV SC
|06:30| D
|07:40| D LV SC
|08:30| D SC
|09:30| A LV
|10:30| A D
|11:30| A D SC LV
|12:25| A LV
|13:00| D
|13:50| A D LV
|15:00| D
|16:00| A SC LV
|17:05|
|18:02| D LV A
|19:10| A D SC
|20:25| SC D
|21:05|
|22:10| D SC
-
LV: Via Lagoa Vermelha
A: Via Aeroclube
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta177(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y7'] + """
|06:05| D
|07:15|
|08:10| D LV
|09:05| D SC
|10:05| D
|11:00|
|11:35| D SC LV
|12:20| A D LV
|14:00| D
|14:30| A
|15:30| SC LV
|16:15|
|16:35| D
|17:00| SC
|17:30| A D LV
|18:15| D LV
|18:42| D LV
|19:18| D SC
|20:05| A LV
|21:00| D
|22:05| D LV SC
|23:00| D LV SC
|00:00| A D
-
LV: Via Lagoa Vermelha
A: Via Aeroclube
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados177(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z7'] + """
Sabados:
|05:10|
|06:00| D LV
|06:40| A SC
|07:30| D SC
|08:30| D
|09:30| D SC LV
|11:30| D
|13:10| A D SC
|14:05| D
|15:50| D SC LV
|17:20| A D SC
|18:10| D
|19:10| A D
|20:40| A D
|21:50| D SC LV
-
Domingos e feriados:
|05:10| D
|06:00| A D LV
|06:30| D
|07:30| D
|08:35| D
|09:45| D
|11:30| D LV
|12:55| A D
|14:20| D
|16:00| A D SC LV
|17:20| A D SC
|18:10| D
|19:20| A D
|20:30| D SC
|21:50| D SC LV
-
LV: Via Lagoa Vermelha
A: Via Aeroclube
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados177(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w7'] + """
Sabados:
|06:15| D
|08:00| D
|09:30| A D LV
|11:00| A D
|12:15| D LV
|12:55| D
|14:00| D
|15:08| D
|15:50| D
|17:14| A D
|18:40| D LV
|19:40| A D LV
|21:30| A D SC
|22:30| D SC
|00:00| A D
-
Domingos e feriados:
|06:15| D
|07:10| D SC
|08:00| D
|09:45| A D SC LV
|11:00| D
|12:30| D
|14:00| D LV
|15:00| A D
|15:50| D SC
|17:14| A D
|18:30| D LV
|19:50| A D LV
|21:40| A D SC
|22:30| D
|00:00| 0A D
-
LV: Via Lagoa Vermelha
A: Via Aeroclube
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"
#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[SsAaDd]ert.*[IiMmAadD]arui.*$")
    def Sertao_do_Maruim_Florianopolis(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Sertao_do_Maruim_Florianopolis

/rota_Sertao_do_Maruim_Florianopolis"""

    @botcmd
    def horario_Sertao_do_Maruim_Florianopolis(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta554
/SaidasCentroSegundaaSexta554
/SaidasBairroSabadosDomingoseFeriados554
/SaidasCentroSabadosDomingoseFeriados554"""
        msg.ctx['x8'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y8'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z8'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w8'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta554(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x8'] + """
|05:45| A
|06:35| A
|07:05| D
|07:40| D SC
|08:10|
|08:30| A D
|09:00| SC
|10:30| SC D
|12:30|
|13:15| SC D
|13:45| SC D
|14:50|
|15:45| SC D
|16:05| SC
|17:00| SC D
|17:15| SC D
|17:40| SC D
|18:55| PE SC
|21:15| SC D
|22:10| SC D
-
PE: Periodo Escolar
A: Via Aeroclube
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta554(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y8'] + """
|06:30| SC
|07:30| EXP SC
|07:50| EXP BR SC
|08:20| SC
|09:50| SC D
|11:15| SC D
|12:10| SC D
|12:57| SC D
|14:15| SC
|14:55| SC D
|15:25| A
|16:12| SC
|16:30| SC D
|16:50| D
|17:10|
|17:57| PE
|18:14| A
|18:40| SC AD
|19:15| A
|20:30| D
|21:25| SC
-
PE: Periodo Escolar
A: Via Aeroclube
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados554(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z8'] + """
Sabados:
|08:30| SC D
|10:20| SC D
|12:20| SC D
|14:10| SC D
|16:50| SC D
|18:20| SC D
|20:00| SC D
-
Domingos e feriados:
|11:30| SC D
|13:00| SC D
|15:30| SC D
|16:50| SC D
|18:20| SC D
|20:00| SC D
-
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados554(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w8'] + """
Sabados:
|09:15| SC D
|11:20| SC D
|12:05| A SC
|13:15| SC D
|16:05| SC D
|17:40| SC D
|19:20| SC D
|20:35| SC D
-
Domingos:
|12:00| SC D
|14:30| SC D
|16:10| D
|17:40| SC D
|19:20| SC D
|20:35| SC D
-
A: Via Aeroclube
SC: Via Shopping Continente
D: Adaptado p/ portadores de necessidades especiais"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"[VvbBCc]ila [FfDdgG]ormo.*$")
    def Vila_Formosa_Florianopolis(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Vila_Formosa_Florianopolis

/rota_Vila_Formosa_Florianopolis"""

    @botcmd
    def horario_Vila_Formosa_Florianopolis(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta5541
/SaidasCentroSegundaaSexta5541
/SaidasBairroSabadosDomingoseFeriados5541
/SaidasCentroSabadosDomingoseFeriados5541"""
        msg.ctx['x9'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y9'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z9'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w9'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta5541(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x9'] + """
|07:00| A
|18:00| SC
-
A: Via Aeroclube
SC: Via Shopping Continente"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta5541(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y9'] + """
|17:10|
|19:15| A
-
A: Via Aeroclube"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados5541(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z9'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados5541(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w9'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------


#===================================ESTRELA========================================

    @botcmd
    def CH_Arthur_Mariano_Circular_Forquilhinha(self, msg, args):
        yield """Ola, o que deseja saber?
    /horario_CH_Arthur_Mariano_Circular_Forquilhinha
    /rota_CH_Arthur_Mariano_Circular_Forquilhinha
"""
    @botcmd
    def horario_CH_Arthur_Mariano_Circular_Forquilhinha(self, msg, args):
        """CH Arthur Mariano"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta651
/SaidasCentroSegundaaSexta651
/SaidasBairroSabadosDomingoseFeriados651
/SaidasCentroSabadosDomingoseFeriados651"""
        msg.ctx['x10'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y10'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z10'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w10'] = 'Saidas do centro de sabados, domingos e feriados:'
    
    @botcmd
    def rota_CH_Arthur_Mariano_Circular_Forquilhinha(self, msg,args):
        yield "https://www.google.com/maps/d/u/0/viewer?mid=1_EI2y_4-DG0XO7xHw0IGTZ2HsjM&ll=-27.602401158879534%2C-48.59874150000002&z=13"

    @botcmd
    def SaidasBairroSegundaaSexta651(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x10'] + """
|06:10|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta651(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y10'] + """
|07:10|
|08:30|
|09:30|
|10:50|
|11:55|
|12:50|
|14:10|
|15:10|
|16:40|
|17:52|
|19:10|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados651(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z10'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados651(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w10'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd 
    def rota_CH_Forquilhinha (self, msg, args):
        yield " https://www.google.com/maps/d/viewer?mid=1YA7m_S1bjBxYMHaOhTTkC1kIieM&ll=-27.6021161740308%2C-48.59941300000003&z=13"
    
    @botcmd
    def CH_Forquilhinha(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_CH_Forquilhinha

/rota_CH_Forquilhinha"""

    @botcmd
    def horario_CH_Forquilhinha(self, msg, args):
        """Linha do Onibus"""
        yield """Escolha o que deseja na proxima mensagem
/SaidasBairroSegundaaSexta117
/SaidasCentroSegundaaSexta117
/SaidasBairroSabadosDomingoseFeriados117
/SaidasCentroSabadosDomingoseFeriados117"""
        msg.ctx['x11'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y11'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z11'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w11'] = 'Saidas do centro de sabados, domingos e feriados:'



    @botcmd
    def SaidasBairroSegundaaSexta117(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x11'] + """
|05:00|
|05:25|
|05:45|
|07:50|
            """
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta117(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y11'] + """
|05:35|
|06:00|
|06:20|
|06:40|
|07:30| E
|07:40|
|08:00|
|08:20|
|08:40|
|09:00|
|09:20|
|09:40|
|10:00|
|10:20|
|10:40|
|11:00|
|11:20|
|11:40|
|12:00|
|12:20|
|12:40|
|13:00|
|13:20|
|13:40|
|14:00|
|14:20|
|14:40|
|15:00|
|15:20|
|15:40|
|16:00|
|16:20|
|16:40|
|17:00|
|17:20|
|17:40|
|18:00|
|18:20|
|18:40|
|19:00|
|19:20|
|19:40|
|20:00|
|20:30|
|21:00|
|22:00|
|22:30| R
|23:00|
        """
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados117(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z11'] + """
Sabado:
|05:30|
|06:00|
Domingos:
|05:30|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados117(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w11'] + """
Sabados:
|06:00|
|06:30|
|07:00|
|07:20|
|07:40|
|08:00|
|08:30|
|09:00|
|09:30|
|10:00|
|10:30|
|11:00|
|11:30|
|12:00|
|12:30|
|13:00|
|13:30|
|14:00|
|14:30|
|15:00|
|15:30|
|16:00|
|16:30|
|17:00|
|17:30|
|18:00|
|18:30|
|19:00|
|19:30|
|20:00|
|20:30|
|21:00|
|21:30|
|22:00|
|22:30|
Domingos:
|06:00|
|07:00|
|08:00|
|09:00|
|10:00|
|11:00|
|12:00|
|13:00|
|14:00|
|15:00|
|16:00|
|17:00|
|18:00|
|19:00|
|20:00|
|21:00|
|22:00|
|23:10|
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
#    @botcmd
#    def rota_Campinas (self, msg, args):
#        yield " "
    
    
    
    @botcmd
    def Campinas(self, msg, args):
        yield """O que você quer saber?
/horario_Campinas

/rota_Campinas"""

    @botcmd
    def horario_Campinas(self, msg, args):
        """Campinas"""
        yield """Saindo de onde?
/SaidasBairroSegundaaSexta317
/SaidasCentroSegundaaSexta317"""
        msg.ctx['x12'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y12'] = 'Saidas do cetro de segunda a sexta:'
        msg.ctx['z12'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w12'] = 'Saidas do centro de sabados, domingos e feriados:'
        
    
    @botcmd
    def SaidasBairroSegundaaSexta317(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x12'] + """
|05:25|
|05:45|
|06:00|
|06:45|
|07:05|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta317(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
             yield msg.ctx['y12'] + """
|06:00|
|06:20|
|06:40|
|07:00|
|07:20|
|07:40|
|08:00|
|08:20|
|08:40|
|09:00|
|09:20|
|09:40|
|10:00|
|10:20|
|10:40|
|11:00|
|11:20|
|11:40|
|11:57|
|12:12|
|12:27|
|12:42|
|12:57|
|13:12|
|13:27|
|13:42|
|13:57|
|14:12|
|14:27|
|14:42|
|14:57|
|15:12|
|15:27|
|15:42|
|15:57|
|16:12|
|16:27|
|16:42|
|16:57|
|17:12|
|17:27|
|17:42|
|17:57|
|18:12|
|18:27|
|18:42|
|18:57|
|19:12|
|19:27|
|19:42|
|19:57|
|20:15|
|20:30|
|20:45|
|21:00|
|21:15|
|21:30|
|21:45|
|22:30|
|22:50|
|23:20|
|00:00| R
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados317(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z12'] + """
Sabados:
|05:30|
|05:55|
Domingos:
|05:55|
|06:25|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados317(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w12'] + """
Sabados:
|06:00|
|06:20|
|06:40|
|07:00|
|07:20|
|07:40|
|08:00|
|08:2O|
|08:40|
|09:00|
|09:20|
|09:40|
|10:00|
|10:20|
|10:40|
|11:00|
|11:20|
|11:40|
|12:00|
|12:15|
|12:30|
|12:45|
|13:00|
|13:15|
|13:30|
|13:45|
|14:00|
|14:20|
|14:40|
|15:00|
|15:20|
|15:40|
|16:05|
|16:30|
|16:55|
|17:20|
|17:45|
|18:1O|
|18:35|
|19:00|
|19:25|
|19:50|
|20:15|
|20:40|
|21:05|
|21:30|
|22:00|
|22:40|
|23:20| R
|00:00| R
Domingos:
|06:30|
|07:00|
|07:30|
|08:00|
|08:30|
|09:00|
|09:30|
|10:00|
|10:30|
|11:00|
|11:30|
|12:00|
|12:30|
|13:00|
|13:30|
|14:00|
|14:30|
|15:00|
|15:30|
|16:00|
|16:30|
|17:00|
|17:30|
|18:00|
|18:30|
|19:00|
|19:30|
|20:00|
|20:30|
|21:00|
|21:30|
|22:00|
|22:30|
|23:00|
|23:30| R
|00:00| R
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
#===================================Ignorar=====================================


 
    @re_botcmd(pattern=r"^[Tt]es.*$")
    def testregex(self, msg, args):
        yield "I matched!"
#===================================Ignorar=====================================

    @re_botcmd(pattern=r"^[CcXxVv]ampin.*[Gg]in.*$")
    def Campinas_Via_Ginasio_de_Esportes(self, msg, args):
        yield """O que você deseja saber?
/horario_Campinas_Via_Ginasio_de_Esportes

/rota_Campinas_Via_Ginasio_de_Esportes"""

    @botcmd
    def horario_Campinas_Via_Ginasio_de_Esportes(self, msg, args):
        """Campinas Ginasio"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta3171
/SaidasCentroSegundaaSexta3171
/SaidasBairroSabadosDomingoseFeriados3171"""
        msg.ctx['x13'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y13'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z13'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w13'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta3171(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x13'] + """
|06:20|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta3171(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y13'] + """
|07:10|
|08:10|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados3171(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z13'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados3171(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w13'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"
#-------------------------------------------------------------------------------------

    @re_botcmd(pattern=r"^[Cc][Ee][Aa][Ss][Aa].*$")
    def CEASA_Via_Santos_Saraiva(self, msg, args):
        yield """O que você quer saber?
/horario_CEASA_Via_Santos_Saraiva

/rota_CEASA_Via_Santos_Saraiva"""

    @botcmd
    def horario_CEASA_Via_Santos_Saraiva(self, msg, args):
        """CEASA Santos Saraiva"""
        yield """Qual das saídas?
/SaidasBairroSegundaaSexta328
/SaidasCentroSegundaaSexta328
/SaidasBairroSabadosDomingoseFeriados328
/SaidasCentroSabadosDomingoseFeriados328"""
        msg.ctx['x14'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y14'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z14'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w14'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta328(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x14'] + """
|06:00|
|06:25|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta328(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y14'] + """
|06:25|
|06:45|
|07:15|
|07:45|
|08:15|
|08:45|
|09:15|
|09:45|
|10:15|
|10:45|
|11:15|
|11:45|
|12:15|
|12:45|
|13:15|
|13:45|
|14:15|
|14:45|
|15:15|
|15:45|
|16:15|
|16:45|
|17:15|
|17:45|
|18:15|
|18:45|
|19:15|
|19:45|
|20:15|
|20:45|
|21:15|
|21:45|
|22:15|
|22:45| R
|23:15| R"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados328(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z14'] + """
Sabados:
|06:00|
|06:30|
.
Domingos e feriados:
|06:05|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados328(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w14'] + """
Sabados:
|06:30|
|07:15|
|08:00|
|08:45|
|09:30|
|10:15|
|11:00|
|11:45|
|12:15|
|13:15|
|14:00|
|14:45|
|15:30|
|16:15|
|17:00|
|17:45|
|18:30|
|19:15|
|20:00|
|20:45|
|21:30|
|22:15| R
|23:15| R
.
Domingos e feriados:
|06:40|
|07:40|
|08:40|
|09:40|
|10:40|
|11:40|
|12:40|
|13:40|
|14:40|
|15:40|
|16:40|
|17:40|
|18:40|
|19:40|
|20:40|
|21:40|
|22:40| R"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[Cc]eniro.*$")
    def Ceniro_Via_Jardim_das_Palmeiras(self, msg, args):
        yield """O que você quer saber?
/horario_Ceniro_Via_Jardim_das_Palmeiras

/rota_Ceniro_Via_Jardim_das_Palmeiras"""

    @botcmd
    def horario_Ceniro_Via_Jardim_das_Palmeiras(self, msg, args):
        """Ceniro Via Jardim das Palmeiras"""
        yield """Qual Saída?
/SaidasBairroSegundaaSexta131
/SaidasCentroSegundaaSexta131
/SaidasBairroSabadosDomingoseFeriados131
/SaidasCentroSabadosDomingoseFeriados131"""
        msg.ctx['x15'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y15'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z15'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w15'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta131(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x15'] + """
05:55
06:15
07:00
07:25
08:15
08:45*
10:50*
12:10
12:50*
13:55*
14:55*
16:00*
18:15*
20:40*"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta131(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y15'] + """
08:05
10:05
12:07
13:10
14:05
15:05
17:15
18:20
19:55
21:55"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados131(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z15'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""        
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados131(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w15'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^.*[Zz]enaide.*$")
    def D_Zenaide_Via_Santa_Felicidade_Ceniro(self, msg, args):
        yield """O que você quer saber?
/horario_D_Zenaide_Via_Santa_Felicidade_Ceniro

/rota_D_Zenaide_Via_Santa_Felicidade_Ceniro"""

    @botcmd
    def horario_D_Zenaide_Via_Santa_Felicidade_Ceniro(self, msg, args):
        """D Zenaide Via Santa Felicidade Ceniro"""
        yield """Qual saída?
/SaidasBairroSegundaaSexta7632
/SaidasCentroSegundaaSexta7632
/SaidasBairroSabadosDomingoseFeriados7632
/SaidasCentroSabadosDomingoseFeriados7632"""
        msg.ctx['x16'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y16'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z16'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w16'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta7632(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x16'] + """
05:40
06:30
06:40
07:05
08:40*
09:25*
10:40*
12:30*
13:35*
14:45*
15:40*
16:35*
17:50*
19:45*"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta7632(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y16'] + """
07:55
08:35
09:50
11:35
12:40
13:50
14:42
15:35
16:50
18:40
20:45
21:45
22:45"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados7632(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z16'] + """
Sabados:
05:50
07:10
08:50*
12:15*
14:15*
17:10*
19:00*
.
Domingos e feriados:
09:15*
11:15*
13:15*
15:15*
17:15*
19:15*"""        
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados7632(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w16'] + """
Sabados:
08:05
11:15
13:20
16:15
18:05
20:05
.
Domingos e feriados:
08:30
10:30
12:30
14:30
16:30
18:30"""        
        except:
            yield "Primeiro informe a linha que deseja"
    
#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[Ee][Xx][Ee][Cc][Uu][Tt][Ii][Vv][Oo].*[Ss]an.*[Mm]arin.*$")
    def EXECUTIVO_San_Marino_Lisboa(self, msg, args):
        yield """O que você quer saber?
/horario_EXECUTIVO_San_Marino_Lisboa

/rota_EXECUTIVO_San_Marino_Lisboa"""

    @botcmd
    def horario_EXECUTIVO_San_Marino_Lisboa(self, msg, args):
        """EXECUTIVO San Marino Lisboa"""
        yield """Qual saída?
/SaidasBairroSegundaaSexta7633
/SaidasCentroSegundaaSexta7633
/SaidasBairroSabadosDomingoseFeriados7633
/SaidasCentroSabadosDomingoseFeriados7633"""
        msg.ctx['x17'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y17'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z17'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w17'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta7633(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x17'] + """
05:45
06:05
06:25
06:45
07:05
07:25
07:45
08:05
08:25
09:00
10:00*
11:00*
11:30
12:00*
12:30
13:00"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta7633(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y17'] + """
09:05
10:00
11:00
12:00
13:00
14:00
14:30
15:00
15:30
16:00
16:20
16:40
17:00
17:20
17:40
18:00
18:15
18:30
18:45
19:00
19:20
19:40
20:00"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados7633(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z17'] + """
Sabados:
06:00
06:30
07:00
07:30
08:00
08:30
09:00
09:30
10:00
10:30
11:00
11:30
12:00
12:30
13:00
13:30
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados7633(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w17'] + """
Sabados:
09:00
09:30
10:00
10:30
11:00
11:30
12:00
12:30
13:00
13:30
14:00
14:30
15:00
15:30
16:00
16:30"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Forquilhas_Florianopolis(self, msg, args):
        yield """O que você quer saber?
/horario_Forquilhas_Florianopolis

/rota_Forquilhas_Florianopolis"""

    @botcmd
    def horario_Forquilhas_Florianopolis(self, msg, args):
        """Forquilhas Florianopolis""" 
        yield """Qual saída?
/SaidasBairroSegundaaSexta0039
/SaidasCentroSegundaaSexta0039
/SaidasBairroSabadosDomingoseFeriados0039
/SaidasCentroSabadosDomingoseFeriados0039"""
        msg.ctx['x18'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y18'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z18'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w18'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta0039(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x18'] + """
05:00
05:40
05:55
06:20
07:00
08:00
08:40
09:50
11:20
12:55
14:25
15:30
16:35
17:35
18:40
19:30
20:20
21:45
23:15"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta0039(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y18'] + """
06:10
07:10
07:45
09:00
10:30
12:00
13:30
14:30
15:30
16:30
17:30
18:30 - Linha C
19:20
20:50
22:20
23:20
00:30"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados0039(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z18'] + """
Sábado: 
05:00
06:00
06:40
07:50
08:20
09:50
11:30
12:30
13:15
15:00
16:55
18:55
20:55
23:25
.
Domingos e Feriados:
05:40
06:30
08:15
09:55
11:55
14:55
17:55
19:55
21:50"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados0039(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w18'] + """
Sábado:s
05:50
06:50
07:30
09:00
10:30
11:30
12:10
14:00
16:00
18:00
20:00
22:30
00:30
.
Domingos e Feriados:
07:30
09:10
11:00
14:00
17:00
19:05
21:00
22:50
00:30
"""
        except:
            yield "Primeiro informe a linha que deseja"


#---------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Forquilhinha_Via_Rodeio_e_Palmares(self, msg, args):
        yield """O que você quer saber?
/horario_Forquilhinha_Via_Rodeio_e_Palmares

/rota_Forquilhinha_Via_Rodeio_e_Palmares"""

    @botcmd
    def horario_Forquilhinha_Via_Rodeio_e_Palmares(self, msg, args):
        """Forquilhinha Via Rodeio e Palmares"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta0392
/SaidasCentroSegundaaSexta0392
/SaidasBairroSabadosDomingoseFeriados0392
/SaidasCentroSabadosDomingoseFeriados0392"""
        msg.ctx['x19'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y19'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z19'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w19'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta0392(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x19'] + """
06:25
06:55
08:05
08:50
09:25
11:25
12:25
13:05
14:00
14:40
15:30
17:10
19:10
21:30"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta0392(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y19'] + """
Linha R: passa no Palmares sentido Centro/Bairro

07:35
08:55
10:50
11:50
12:30
13:25
14:05
14:55
16:25
17:20 - Linha R
18:15
19:20
20:55
22:22 - Linha R"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados0392(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z19'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados0392(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w19'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#---------------------------------------------------------------------------------------------------------------------------------------------------

    @botcmd
    def Kobrasol(self, msg, args):
        yield """O que você quer saber?
/horario_Kobrasol

/rota_Kobrasol"""

    @botcmd
    def horario_Kobrasol(self, msg, args):
        """Kobrasol"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta0141
/SaidasCentroSegundaaSexta0141
/SaidasBairroSabadosDomingoseFeriados0141
/SaidasCentroSabadosDomingoseFeriados0141"""
        msg.ctx['x20'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y20'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z20'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w20'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta0141(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x20'] + """
06:05           
06:20        
06:30       
06:40       
06:50       
07:00               
07:10           
07:31           
07:53       
08:15           
08:35       
08:55
09:15
09:35
09:55
10:15
10:37
10:57
11:17
11:37
11:57
12:17
12:32
12:49
13:02
13:17
13:32
13:47
14:03
14:18
14:33
14:48
15:03
15:19
15:34
15:49
16:04
16:19
16:34
16:49
17:04
17:19
17:34
17:49
18:04
18:20
18:35
18:50
19:05
19:19
19:34
19:45
20:00
20:15
20:28"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta0141(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y20'] + """
06:10 
06:30   
06:50   
07:10   
07:30           
07:50           
08:10 
08:30   
08:50   
09:10   
09:30
09:50
10:10
10:30
10:50
11:10
11:30
11:50
12:05
12:20
12:35
12:50
13:05
13:20
13:35
13:50
14:05
14:20
14:35
14:50
15:05
15:20
15:35
15:50
16:05
16:20
16:35
16:50
17:05
17:20
17:35
17:50
18:05
18:20
18:35
18:50
19:05
19:20
19:35
19:50
20:05"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados0141(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z20'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados0141(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w20'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[KkJjLl]obrasol.*[Vv][Ii][Pp].*$")
    def Kobrasol_VIP(self, msg, args):
        yield """O que você quer saber?
/horario_Kobrasol_VIP

/rota_Kobrasol_VIP"""

    @botcmd
    def horario_Kobrasol_VIP(self, msg, args):
        """Kobrasol VIP"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta1412
/SaidasCentroSegundaaSexta1412
/SaidasBairroSabadosDomingoseFeriados1412
/SaidasCentroSabadosDomingoseFeriados1412"""
        msg.ctx['x21'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y21'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z21'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w21'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta1412(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x21'] + """
06:20
06:35
06:50
07:05
07:20"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta1412(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y21'] + """
Linha R: Só sentido de volta

07:20
07:35
07:50
08:05
08:20
08:40
08:55
09:25
10:00
10:30
11:00
11:30
11:50
12:10
12:30
12:50
13:10
13:30
14:00
14:30
14:50
15:10
15:35
16:10
16:30
16:50
17:10
17:30
17:50
18:10
18:30
18:50 - Linha R
19:10 - Linha R
19:30 - Linha R
19:55 - Linha R
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados1412(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z21'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados1412(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w21'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[LlKk]os.*[AasS]ngele.*$")
    def Los_Angeles(self, msg, args):
        yield """O que você quer saber?
/horario_Los_Angeles

/rota_Los_Angeles"""

    @botcmd
    def horario_Los_Angeles(self, msg, args):
        """Los Angeles"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta763
/SaidasCentroSegundaaSexta763
/SaidasBairroSabadosDomingoseFeriados763
/SaidasCentroSabadosDomingoseFeriados763"""
        msg.ctx['x22'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y22'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z22'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w22'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta763(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x22'] + """
Linha E: Extensão
Linha L:Lisboa
Linha M: Via Loteamento Melo
Linha R: Via Rodeio
Linha Z: Via Zenaide

05:15 - Linhas Z e R
05:40
06:00 - Linhas E, Z e R
06:15 - Expresso
06:25
06:50 - Linha Z
07:05 - Linha Z
07:20 - Linha M
08:00 - Linha Z
09:00
09:25 - Linha M
10:00 - Linha Z
10:55
11:50
12:35
13:05 - Linha E
14:15 - Linha M
15:20
16:20
17:15 - Linhas E e Z
18:20 - Expresso
19:35 - Linha E
20:20 - Linhas Z e R
21:10 - Linhas E e Z
"""        
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta763(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y22'] + """
Linha E: Extensão
Linha L:Lisboa
Linha M: Via Loteamento Melo
Linha R: Via Rodeio
Linha Z: Via Zenaide

06:12 - Linha Z
06:30 - Linhas L e M
08:15 - Linha R
08:40 - Linha M
09:15 - Linha Z
10:10
11:05
11:40 - Linha M
12:10 - Linhas Z e E
13:20 - Linha M
14:10 - Linha Z
15:15
16:10 - Linhas Z e E
16:35 - Linha M
17:03 - Linhas Z e E
17:33
18:25 - Linhas Z e E
18:50 - Linha 
19:17 - Linha Z
20:05 - Linhas E,R e Z"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados763(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z22'] + """
Linha E: Extensão
Linha L:Lisboa
Linha M: Via Loteamento Melo
Linha R: Via Rodeio
Linha Z: Via Zenaide

Sábado:
06:00 - Linha R
06:30 - Linha Z
07:55 - Linhas Z e R
10:05 - Linhas Z e R
11:40 - Linha R
13:25 - Linhas Z e R
14:15 - Linha R
16:05 - Linhas Z e R
18:05 - Linhas Z e R
20:05 - Linhas Z e R
.
Domingos e feriados:
06:20 - Linhas Z, L e R
08:10 - Linhas Z e R
10:25 - Linhas Z e R
12:25 - Linhas Z e R
14:25 - Linhas Z e R
16:25 - Linhas Z e R
18:25 - Linhas Z e R
20:25 - Linhas Z e R
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados763(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w22'] + """
Linha E: Extensão
Linha L:Lisboa
Linha M: Via Loteamento Melo
Linha R: Via Rodeio
Linha Z: Via Zenaide

Sábado:
07:05 - Linhas R e Z
09:10 - Linhas R e Z
10:45 - Linha R
12:25 - Linhas R e Z
13:15 - Linha R
15:05 - Linhas R e Z
17:05 - Linhas R e Z
19:05 - Linhas R e Z
22:05 - Linhas R e Z

Domingos e Feriados:
07:20 - Linhas R e Z
09:30 - Linhas R e Z
11:30 - Linhas R e Z
13:30 - Linhas R e Z
15:30 - Linhas R e Z
17:30 - Linhas R e Z
19:30 - Linhas R e Z
22:30 - Linhas R e Z"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Parque_Residencial_Lisboa(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Parque_Residencial_Lisboa

/rota_Parque_Residencial_Lisboa"""
    
    @botcmd
    def PR_Lisboa(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Parque_Residencial_Lisboa

/rota_Parque_Residencial_Lisboa"""
    
    @botcmd
    def P_R_Lisboa(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Parque_Residencial_Lisboa

/rota_Parque_Residencial_Lisboa"""

    @botcmd
    def horario_Parque_Residencial_Lisboa(self, msg, args):
        """Parque Residencial Lisboa"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta7631
/SaidasCentroSegundaaSexta7631
/SaidasBairroSabadosDomingoseFeriados7631
/SaidasCentroSabadosDomingoseFeriados7631"""
        msg.ctx['x23'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y23'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z23'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w23'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta7631(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x23'] + """
Linha BR: Via BR101
Linha LA: Via Los Angeles

05:00
05:30
05:45
06:00
06:12
06:25
06:37
06:50 - Linhas BR
07:02
07:15
07:30 - Linhas BR
07:45
08:05
08:30
08:55
10:20
11:15
12:05
12:25
12:50
13:25
13:45 - Linhas BR
14:30
15:25
15:35
16:20
16:55
17:15 - Linhas BR
17:35
18:10
19:10
19:35
20:05
20:55
21:45
22:25
22:55"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta7631(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y23'] + """
Linha BR: Via BR101
Linha LA: Via Los Angeles

06:40
07:25
07:50
08:15
08:42
09:35
10:32
11:20
12:02
12:35
13:05
13:42
14:35
14:50
15:25
16:00
16:20
16:40
16:55
17:05
17:15
17:25
17:37
17:50
18:05
18:20
18:35
18:55
19:10
19:40
20:15
21:05
21:30 - Linhas LA
22:05
22:15 - Linhas LA
22:35 - Linhas LA
23:05 - Linhas LA
23:35
00:00"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados7631(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z23'] + """
Sábado:
06:00
06:30
07:00
07:15
07:30
07:45
08:25
09:15
10:50
11:55
12:45
13:30
14:25
15:25
16:25
17:20
18:15
19:20
20:20
20:55
22:20

Domingos e Feriados:
07:00
08:30
09:30
10:30
11:30
12:30
13:30
14:30
15:30
16:30
17:30
18:30
19:30
20:30
21:30
22:30"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados7631(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w23'] + """
Sábado:
06:40
07:50
08:35
10:10
11:05
12:00
12:45
13:40
14:40
15:40
16:35
17:30
18:35
19:35
20:10
21:35
22:45
00:00

Domingos e Feriados:
07:00
08:30
09:30
10;30
11:30
12:30
13:30
14:30
15:30
16:30
17:30
18:30
19:30
20:30
21:30
22:30
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Potecas(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Potecas

/rota_Potecas"""

    @botcmd
    def horario_Potecas(self, msg, args):
        """Potecas"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta0020
/SaidasCentroSegundaaSexta0020
/SaidasBairroSabadosDomingoseFeriados0020
/SaidasCentroSabadosDomingoseFeriados0020"""
        msg.ctx['x24'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y24'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z24'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w24'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta0020(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x24'] + """
Linha A: Até o ponto final do Arruda

05:00
05:20
06:00
06:30
06:45
07:00
07:35
08:05
09:00
10:00
11:05
12:00
13:00
13:30
14:40
15:45
16:50
17:45
18:45
19:40
20:45
21:25
22:40"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta0020(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y24'] + """
Linha A: Até o ponto final do Arruda

06:45
07:15
08:10
19:10
10:15
11:10
12:05
12:38
13:45
14:45
15:45
16:25
16:40
17:35
18:02
18:35
19:05
19:50
20:35
21:50
22:40
12:50 - Linha A
13:30 - Linha A
14:30 - Linha A
15:00 - Linha A
15:30 - Linha A
16:30 - Linha A
17:05 - Linha A
17:35 - Linha A
18:15 - Linha A
19:05 - Linha A
19:45 - Linha A
20:45 - Linha A
21:12 - Linha A
22:35 - Linha A
23:05 - Linha A"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados0020(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z24'] + """
Linha A: Até o ponto final do Arruda

Sábaos:
05:25 - Linha A
05:55 - Linha A
06:20 - Linha A
06:50 - Linha A
07:12 - Linha A
07:30 - Linha A
08:00 - Linha A
08:40 - Linha A
09:10 - Linha A
09:50 - Linha A
10:25 - Linha A
11:05 - Linha A
11:25 - Linha A
12:10 - Linha A

Domingos e Feriados:
06:05 - Linha A
07:05 - Linha A
08:00 - Linha A
09:00 - Linha A
10:00 - Linha A
11:00 - Linha A
12:00 - Linha A
13:00 - Linha A
14:00 - Linha A
15:00 - Linha A
16:00 - Linha A
17:00 - Linha A
18:00 - Linha A
19:00 - Linha A
20:00 - Linha A
21:00 - Linha A
22:00 - Linha A"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados0020(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w24'] + """
Linha A: Até o ponto final do Arruda

Sábado:
06:20 - Linha A
06:40 - Linha A
07:10 - Linha A
07:45 - Linha A
08:15 - Linha A
08:55 - Linha A
09:35 - Linha A
10:05 - Linha A
10:25 - Linha A
11:05 - Linha A
11:55 - Linha A
12:35 - Linha A
13:35 - Linha A
14:05 - Linha A
14:35 - Linha A
15:35 - Linha A
16:10 - Linha A
16:40 - Linha A
17:20 - Linha A
18:10 - Linha A
18:40 - Linha A
19:40 - Linha A
20:15 - Linha A
21:40 - Linha A
22:10 - Linha A
23:20 - Linha A

Domingos e Feriados:
07:15 - Linha A
08:15 - Linha A
09:15 - Linha A
10:15 - Linha A
11:15 - Linha A
12:15 - Linha A
13:15 - Linha A
14:15 - Linha A
15:15 - Linha A
16:15 - Linha A
17:15 - Linha A
18:15 - Linha A
19:15 - Linha A
20:15 - Linha A
21:15 - Linha A
22:15 - Linha A
23:30 - Linha A"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Potecas_Santos_Saraiva(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Potecas_Santos_Saraiva

/rota_Potecas_Santos_Saraiva"""

    @botcmd
    def horario_Potecas_Santos_Saraiva(self, msg, args):
        """Potecas Santos Saraiva"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta0201
/SaidasCentroSegundaaSexta0201
/SaidasBairroSabadosDomingoseFeriados0201
/SaidasCentroSabadosDomingoseFeriados0201"""
        msg.ctx['x25'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y25'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z25'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w25'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta0201(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x25'] + """
Linha A: Até o ponto final do Arruda

05:35
06:10
06:50
07:10
07:45
08:30
09:30
10:30
11:30
12:30
13:40
14:55
16:10
17:05
18:25
22:10 - Linha A"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta0201(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y25'] + """
Linha A: Até o ponto final do Arruda

06:15
07:05
07:42
08:45
09:45
10:45
11:40
12:55
14:10
15:12
16:08
16:55
17:20
17:48
18:17
18:50
19:30
20:10
21:20 - Linha A
22:15
23:33 - Linha A"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados0201(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z25'] + """
OBS:. Nesses dias a linhas vai até o ponto final do Arruda

Sábado:
|05:25| 
|05:55|
|06:20| 
|06:50| 
|07:12| 
|07:30|
|08:00| 
|08:40| 
|09:10| 
|09:50|
|10:25| 
|11:05| 
|11:25|
|12:10| 

Domingos e Feriados:
06:05 - Linha A
07:05 - Linha A
08:00 - Linha A
09:00 - Linha A
10:00 - Linha A
11:00 - Linha A
12:00 - Linha A
13:00 - Linha A
14:00 - Linha A
15:00 - Linha A
16:00 - Linha A
17:00 - Linha A
18:00 - Linha A
19:00 - Linha A
20:00 - Linha A
21:00 - Linha A
22:00 - Linha A"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados0201(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w25'] + """
Linha A: Até o ponto final do Arruda

Sábados

06:20 - Linha A
06:40 - Linha A
07:10 - Linha A
07:45 - Linha A
08:15 - Linha A
08:55 - Linha A
09:35 - Linha A
10:05 - Linha A
10:25 - Linha A
11:05 - Linha A
11:55 - Linha A
12:35 - Linha A
13:35 - Linha A
14:05 - Linha A
14:35 - Linha A
15:35 - Linha A
16:10 - Linha A
16:40 - Linha A
17:20 - Linha A
18:10 - Linha A
18:40 - Linha A
19:40 - Linha A
20:15 - Linha A
21:40 - Linha A
22:10 - Linha A
23:20 - Linha A

Domingos e Feriados

07:15 - Linha A
08:15 - Linha A
09:15 - Linha A
10:15 - Linha A
11:15 - Linha A
12:15 - Linha A
13:15 - Linha A
14:15 - Linha A
15:15 - Linha A
16:15 - Linha A
17:15 - Linha A
18:15 - Linha A
19:15 - Linha A
20:15 - Linha A
21:15 - Linha A
22:15 - Linha A
23:30 - Linha A
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[RrEeTt]ecanto.*[NnMmBb]ature.*$")
    def Recanto_da_Natureza_Via_Ceniro_Martins(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Recanto_da_Natureza_Via_Ceniro_Martins

/rota_Recanto_da_Natureza_Via_Ceniro_Martins"""

    @botcmd
    def horario_Recanto_da_Natureza_Via_Ceniro_Martins(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta0202
/SaidasCentroSegundaaSexta0202
/SaidasBairroSabadosDomingoseFeriados0202
/SaidasCentroSabadosDomingoseFeriados0202"""
        msg.ctx['x26'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y26'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z26'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w26'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta0202(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x26'] + """
|05:50|
|06:50|
|07:15|
|07:40|
|09:00|
|09:55|
|11:20|
|12:10|
|12:55|
|13:10|
|14:50|
|16:25|
|16:50|
|19:00|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta0202(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y26'] + """
|07:00|
|09:05|
|10:35|
|11:25|
|11:55|
|12:25|
|14:00|
|15:25|
|15:55|
|17:10|
|17:40|
|18:10|
|19:10|
|21:10|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados0202(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z26'] + """
Sabado: 
|06:15|
|07:30|
|09:15|
|12:55|
|14:55|
|18:15|
|20:00|

Domingo nao funciona"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados0202(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w26'] + """
Sabados
|08:30|
|12:15|
|14:10|
|17:30|
|19:15|

Domingo nao funciona"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[Ss]ao.*[Ll]ui.*$")
    def Bairro_Sao_Luiz(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Bairro_Sao_Luiz

/rota_Bairro_Sao_Luiz"""

    @botcmd
    def horario_Bairro_Sao_Luiz(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta0142
/SaidasCentroSegundaaSexta0142
/SaidasBairroSabadosDomingoseFeriados0142
/SaidasCentroSabadosDomingoseFeriados0142"""
        msg.ctx['x27'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y27'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z27'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w27'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta0142(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x27'] + """
|06:00|
|08:30|
|10:00|
|12:15|
|15:05|
|17:10|
|19:00|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta0142(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y27'] + """
|08:02|
|09:30|
|11:45|
|14:30|
|16:25|
|18:15|
|22:30|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados0142(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z27'] + """
Sabados: 
|07:20|
|08:30|
|10:00|
|12:45|

Domingos e Feriados:
|07:20|
|08:30|
|10:00|
|12:45|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados0142(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w27'] + """
Sabados:

|09:30|
|12:15|

Domingos e Feriados:

|09:30|
|12:15|
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[SsAaFf]erraria.*$")
    def Serraria_Forquilhinha(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Serraria_Forquilhinhas

/rota_Serraria_Forquilhinhas"""

    @botcmd
    def horario_Serraria_Forquilhinhas(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?  só para avisar: Essa liha é feita pelas empresas Bguaçu, Estrela e Jotur, entao por mais que os horarios sejam os mesmos, os onibus podem vaiar.
/SaidasSerrariaSegundaaSexta0105
/SaidasForquilhinhasSegundaaSexta0105
/SaidasSerrariaSabadosDomingoseFeriados0105
/SaidasForquilhinhasSabadosDomingoseFeriados0105"""
        msg.ctx['x28'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y28'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z28'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w28'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasSerrariaSegundaaSexta0105(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x28'] + """
|05:30|
|06:20|
|06:30|
|07:20|
|08:30|
|09:30|
|10:30|
|11:30|
|12:15|
|12:40|
|13:40|
|14:40|
|15:30|
|16:30|
|17:00|
|18:50|
|19:30|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasForquilhinhasSegundaaSexta0105(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y28'] + """
|05:50|
|07:00|
|07:50|
|09:00|
|10:00|
|11:00|
|11:35|
|12:00|
|13:00|
|13:50|
|14:50|
|15:30|
|17:05|
|17:35|
|18:10|
|19:00|
|20:20|
|22:20|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasSerrariaoSabadosDomingoseFeriados0105(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z28'] + """
Sabados:
|05:30|
|07:15|
|10:00|
|11:40|
Domingos: Nao opera
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasForquilhinhasSabadosDomingoseFeriados0105(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w28'] + """
Sabados:
|06:00|
|07:50|
|10:20|
|12:10|
|13:50|
Domingos: Nao opera"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[BbVvNn]arreiros.*[SsdDaA]ed.*$")
    def Barreiros_Sede(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Barreiros_Sede

/rota_Barreiros_Sede"""

    @botcmd
    def horario_Barreiros_Sede(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida? E so para avisar: Essa linha pode ser feita pelas empresas Biguaçu, Estrela ou Jotur,enao por mais que os horarios sejam os mesmos, os onibus podem variar.
/SaidasBarreirosSegundaaSexta0110
/SaidasSedeSegundaaSexta0110
/SaidasBarreirosSabadosDomingoseFeriados0110
/SaidasSedeSabadosDomingoseFeriados0110"""
        msg.ctx['x29'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y29'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z29'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w29'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBarreirosSegundaaSexta0110(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x29'] + """
|06:05|
|06:55|
|08:00|
|10:30|
|11:30|
|12:20|
|13:30|
|14:30|
|15:30|
|16:30|
|17:30|
|19:05|
|21:00|
|21:45|
|22:30|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasSedeSegundaaSexta0110(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y29'] + """
|06:00|
|07:05|
|08:20|
|10:00|
|11:20|
|12:30|
|13:20|
|14:30|
|15:40|
|16:30|
|17:40|
|19:10|
|21:00|
|21:45|
|22:30|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados0110(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z29'] + """
Sabados:
|07:00|
Domingos: Nao opera"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados0110(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w29'] + """
Sabados:
|12:00|
Domingos: Nao opera"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Forquilhas_Kobrasol(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Forquilhas_Kobrasol

/rota_Forquilhas_Kobrasol"""

    @botcmd
    def horario_Forquilhas_Kobrasol(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasForquilhasSegundaaSexta0120
/SaidasKobrasolSegundaaSexta0120
/SaidasForquilhasSabadosDomingoseFeriados0120
/SaidasKobrasolSabadosDomingoseFeriados0120"""
        msg.ctx['x30'] = 'Saidas de Forquilhas de segunda a sexta:'
        msg.ctx['y30'] = 'Saidas do Kobrasol de segunda a sexta:'
        msg.ctx['z30'] = 'Saidas de Forquilhas de sabados, domingos e feriados:'
        msg.ctx['w30'] = 'Saidas do Kobrasol de sabados, domingos e feriados:'

    @botcmd
    def SaidasForquilhasSegundaaSexta0120(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x30'] + """
|05:40|
|06:20|
|07:20|
|08:30|
|09:20|
|11:20|
|12:20|
|13:10|
|14:30|
|16:30|
|17:30|
|17:50|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasKobrasolSegundaaSexta0120(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y30'] + """
|06:30|
|07:15|
|08:20|
|10:30|
|11:20|
|13:30|
|15:30|
|16:35|
|17:00|
|17:30|
|18:30|
|19:30|
|22:30|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasForquilhasSabadosDomingoseFeriados0120(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z30'] + """
Sabados:
|06:10|
|07:00|
|08:35|
|09:00|
|10:10|
|11:00|
|12:20|
|13:00|
|14:30|
|15:50|
|16:50|
|17:50|
|19:00|
|20:10|
|22:10|
|23:00|
Domingos:
|07:00|
|09:20|
|11:10|
|13:10|
|13:30|
|15:20|
|16:20|
|17:20|
|18:20|
|20:00|
|21:20|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasKobrasolSabadosDomingoseFeriados0120(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w30'] + """
Sabados:
|07:30|
|08:10|
|09:10|
|10:00|
|11:20|
|12:00|
|13:35|
|14:50|
|15:50|
|16:50|
|18:00|
|19:00|
|21:10|
|22:00|
Domingos:
|08:30|
|10:20|
|12:10|
|12:40|
|14:20|
|15:20|
|16:20|
|17:20|
|19:00|
|20:30|
|22:10|"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[VvCcbB]ila.*$")
    def Vila_Formosa(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Vila_Formosa

/rota_Vila_Formosa"""

    @botcmd
    def horario_Vila_Formosa(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasVilaFormosaSegundaaSexta0125
/SaidasKobrasolSegundaaSexta0125
/SaidasVilaFormosaSabadosDomingoseFeriados0125
/SaidasKobrasolSabadosDomingoseFeriados0125"""
        msg.ctx['x31'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y31'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z31'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w31'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasVilaFormosaSegundaaSexta0125(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x31'] + """
|06:00|
|06:20|
|06:45|
|07:20|
|08:10|
|09:05|
|09:50|
|12:05|
|12:30|
|12:40|
|13:50|
|14:30|
|16:10|
|17:00|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasKobrasolSegundaaSexta0125(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y31'] + """
|06:40|
|07:20|
|09:00|
|11:10|
|11:50|
|13:00|
|13:40|
|15:20|
|16:10|
|17:40|
|18:10|
|18:40|
|19:30|
|22:25|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasVilaFormosaSabadosDomingoseFeriados0125(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z31'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasKobrasolSabadosDomingoseFeriados0125(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w31'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[DdSsFf]iret.*")
    def Diretao(self, msg, args):
        yield """Oi, o que voce gostaria de saber?
/horario_Diretao

/rota_Diretao"""

    @botcmd
    def horario_Diretao(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBarreirosSegundaaSexta0130
/SaidasFazendaSegundaaSexta0130
/SaidasBarreirosSabadosDomingoseFeriados0130
/SaidasFazendaSabadosDomingoseFeriados0130"""
        msg.ctx['x32'] = 'Saidas de barreiros de segunda a sexta:'
        msg.ctx['y32'] = 'Saidas da Fazenda de segunda a sexta:'
        msg.ctx['z32'] = 'Saidas de barreiros de sabados, domingos e feriados:'
        msg.ctx['w32'] = 'Saidas da Fazenda de sabados, domingos e feriados:'

    @botcmd
    def SaidasBarreirosSegundaaSexta0130(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x32'] + """
|06:25|
|07:00|
|07:30|
|08:10|
|09:00|
|09:50|
|10:20|
|11:20|
|12:00|
|12:25|
|12:45|
|13:05|
|13:35|
|14:10|
|14:40|
|15:30|
|16:20|
|17:00|
|17:30|
|18:00|
|19:00|
|20:00|
|21:00|
|22:00|
|23:00|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasFazendaSegundaaSexta0130(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y32'] + """
|06:40|
|07:20|
|07:50|
|08:20|
|09:20|
|10:20|
|11:15|
|11:40|
|12:00|
|12:20|
|12:50|
|13:20|
|13:50|
|14:30|
|15:00|
|15:30|
|16:10|
|16:40|
|17:10|
|17:30|
|17:50|
|18:10|
|18:30|
|19:00|
|20:00|
|21:00|
|21:50|
|22:40|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBarreirosSabadosDomingoseFeriados0130(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z32'] + """
Sabados:
|06:30|
|07:00|
|07:30|
|08:10|
|08:40|
|09:10|
|09:50|
|10:20|
|11:20|
|12:00|
|14:00|
|17:00|
|19:30|
Domingos:
|07:30|
|09:30|
|12:20|
|14:30|
|16:10|
|17:50|
|20:40|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasFazendaSabadosDomingoseFeriados0130(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w32'] + """
Sabados:
|06:50|
|07:20|
|07:50|
|08:20|
|09:00|
|09:30|
|10:30|
|11:10|
|11:40|
|12:10|
|12:50|
|15:30|
|18:15|
|20:30|
Domingos:
|06:30|
|08:30|
|11:30|
|13:30|
|15:20|
|17:00|
|19:50|"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[PpOo]otecas.*[KkJjLl]obras.*")
    def Potecas_Kobrasol(self, msg, args):
        yield """Oi, que voce gostaria de saber?
/horario_Potecas_Kobrasol

/rota_Potecas_Kobrasol"""

    @botcmd
    def horario_Potecas_Kobrasol(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasPotecasSegundaaSexta0135
/SaidasKobrasolSegundaaSexta0135
/SaidasPotecasSabadosDomingoseFeriados0135
/SaidasKobrasolSabadosDomingoseFeriados0135"""
        msg.ctx['x33'] = 'Saidas do Potecas de segunda a sexta:'
        msg.ctx['y33'] = 'Saidas do Kobrasol de segunda a sexta:'
        msg.ctx['z33'] = 'Saidas do Potecas de sabados, domingos e feriados:'
        msg.ctx['w33'] = 'Saidas do Kobrasol de sabados, domingos e feriados:'

    @botcmd
    def SaidasPotecasSegundaaSexta0135(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x33'] + """
06:20
12:40"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasKobrasolSegundaaSexta0135(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y33'] + """
11:45
17:45"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasPotecasSabadosDomingoseFeriados0135(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z33'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasKobrasolSabadosDomingoseFeriados0135(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w33'] + """
Esse onibus nao tem horario nesses dias, quer voltar ao menu das empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[Ee][Xx][Ee][Cc][Uu][Tt][Ii][Vv][Oo].*[Dd]iret.*")
    def EXECUTIVO_Diretao(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_EXECUTIVO_Diretao

/rota_EXECUTIVO_Diretao"""

    @botcmd
    def horario_EXECUTIVO_Diretao(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBarreirosSegundaaSexta0140
/SaidasFazendaSegundaaSexta0140
/SaidasBarreirosSabadosDomingoseFeriados0140
/SaidasFazendaSabadosDomingoseFeriados0140"""
        msg.ctx['x34'] = 'Saidas de Barreiros de segunda a sexta:'
        msg.ctx['y34'] = 'Saidas da Fazenda/Shopping de segunda a sexta:'
        msg.ctx['z34'] = 'Saidas de Barreiros de sabados, domingos e feriados:'
        msg.ctx['w34'] = 'Saidas da Fazenda/Shopping de sabados, domingos e feriados:'

    @botcmd
    def SaidasBarreirosSegundaaSexta0140(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x34'] + """
06:20
06:50
07:20
08:40
09:10
11:05
11:55
12:40
12:55
14:30
15:10
16:50
18:00
18:30
19:00"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasFazendaSegundaaSexta0140(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y34'] + """06:10
07:10
07:20
08:00
08:30
11:00
11:30
11:50
13:10
13:40
14:20
17:00
17:20
17:40
19:10
19:50"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBarreirosSabadosDomingoseFeriados0140(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z34'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""

        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasFazendaSabadosDomingoseFeriados0140(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w34'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

#==============================================Biguacu====================================
#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Circular_Barreiros(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Circular_Barreiros

/rota_Circular_Barreiros"""

    @botcmd
    def horario_Circular_Barreiros(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta90900
/SaidasBairroSabadosDomingoseFeriados90900"""
        msg.ctx['x35'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['z35'] = 'Saidas do bairro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta90900(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x35'] + """
|05:50|
|06:05|
|07:55|
|08:00|
|08:55|
|09:35|
|10:35|
|11:25|
|11:50|
|12:35|
|13:40|
|14:50|
|15:50|
|16:45|
|17:55|
|19:10|
|20:00|
|21:40|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados90900(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z35'] + """
Sabado

06:15
08:00
09:10
10:45
12:25
13:35
15:10
16:00
17:05
18:45
21:40

Domingo

06:20
08:00
10:00
12:30
14:00
16:20
18:10
19:55"""
        except:
            yield "tente novamente"
#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Bom_Viver(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Bom_Viver

/rota_Bom_Viver"""

    @botcmd
    def horario_Bom_Viver(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta10000
/SaidasCentroSegundaaSexta10000
/SaidasBairroSabadosDomingoseFeriados10000
/SaidasCentroSabadosDomingoseFeriados10000"""
        msg.ctx['x36'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y36'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z36'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w36'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta10000(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x36'] + """
05:25
05:55
06:20
06:40
07:00
07:22
07:41
08:00
08:32
09:05
10:12
11:10
11:50
12:28
12:57
13:33
14:21
15:13
16:05
46:45
17:30
18:02
18:27
20:23
21:37
22:20"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta10000(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y36'] + """
06:15
06:46
07:55
09:35
10:30
11:10
11:45
12:20
12:55
13:40
14:35
15:20
16:00
16:40
17:05
17:30
18:05
18:35
19:00
19:20
19:45
20:15
21:00
21:40
22:20
22:55
24:05
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados10000(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z36'] + """
Sabados:

06:00
06:30
06:55
07:10
07:40
08:05
08:30
09:05
09:30
10:15
11:10
12:00
12:35
13:00
13:40
14:20
15:35
16:50
18:05
19:20
20:40
23:15

Dom. e feriados:

06:00
07:30
09:00
10:30
11:45
12:55
14:05
15:25
16:45
17:35
18:35
19:35
20:35
21:50
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados10000(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w36'] + """
Sábados

06:35
07:05
07:50
08:30
08:55
09:30
10:30
11:20
12:00
12:15
12:30
13:00
13:45
15:00
16:20
17:35
18:50
20:10
21:30
22:45
24:00

Dom. e feriados

06:45
08:15
09:45
11:10
12:25
13:35
14:50
16:10
17:00
18:00
19:00
20:00
21:15
22:30
24:00
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Tres_Riachos(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Tres_Riachos

/rota_Tres_Riachos"""

    @botcmd
    def horario_Tres_Riachos(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta44800
/SaidasCentroSegundaaSexta44800
/SaidasBairroSabadosDomingoseFeriados44800
/SaidasCentroSabadosDomingoseFeriados44800"""
        msg.ctx['x37'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y37'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z37'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w37'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta44800(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x37'] + """
04:30 GUIMARA
05:20
09:45
11:30 R.Velha - P Andrade - Guimara
17:20 R.Velha - P Andrade - Guimara"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta44800(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y37'] + """
07:05 R.Velha - P Andrade - Canudos
10:10 R.Velha - Paulo Andrade
12:15R.Velha - P Andrade - Canudos
15:45
17:00 Canudos - P andrade"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados44800(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z37'] + """
Sabados:
05:00 Velha - P Andrade - Canudos
06:30 Velha - P Andrade - Canudos
15:00 P Andrade - Canudos
Domingos e Feriados:
06:30
16:30
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados44800(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w37'] + """
Sabados:
10:30 Velha - P Andrade - Canudos
13:00 Velha - P Andrade - Canudos
17:00 P Andrade -Canudos
Domingos e Feirados:
08:00 R velha
18:00"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Tres_Riachos_Viaduto_Janaina(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Tres_Riachos_Viaduto_Janaina

/rota_Tres_Riachos_Viaduto_Janaina"""

    @botcmd
    def horario_Tres_Riachos_Viaduto_Janaina(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta44801
/SaidasBiguacuSegundaaSexta44801
/SaidasBairroSabadosDomingoseFeriados44801
/SaidasBiguacuSabadosDomingoseFeriados44801"""
        msg.ctx['x38'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y38'] = 'Saidas de Biguacu de segunda a sexta:'
        msg.ctx['z38'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w38'] = 'Saidas de Biguacu de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta44801(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x38'] + """
06:05 P Andrade - Guiomar
06:20 R Velha - Granja
06:35 ENCR - RVE - Morro -PAND
09:00 R Velha - P Andrade
11:50 Sai COL Rodao p/ Biguacu
12:30 Canudos - P Andrade - Morro
12:31
13:00 R Velha - P Andrade
16:45 Sai Inicio R Velha - Laranjeiras - Morro - P Andrade
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBiguacuSegundaaSexta44801(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y38'] + """
07:05
11:30 Guiomar - R Velha
11:35 Saida Colegio Donato p/ Colegio Rodao
11:41 Saida Rodao p/ Tres Riachos
11:50 Guimara
15:40 Guimara - R velha - Laranjeiras - Morro
17:00 Guimara - Laranjeiras - P Andrade - Canudos
17:30 Guimara - R Velha
18:00 R Velha - P Andrade
19:10 Passa em todas as ruas
22:40
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados44801(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z38'] + """
Sabados:
08:50 Smarcos - P Andrade - Viaduto Janaina
13:00 Smarcos - P Andrade - Viaduto Janaina
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBiguacuSabadosDomingoseFeriados44801(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w38'] + """
Sabados:
08:00 Viaduto Janaina - Sao Marcos - P Andrade - Canudos
12:10
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Tijucas(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Tijucas

/rota_Tijucas"""

    @botcmd
    def horario_Tijucas(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta64300
/SaidasBiguacuSegundaaSexta64300
/SaidasBairroSabadosDomingoseFeriados64300
/SaidasBiguacuSabadosDomingoseFeriados64300"""
        msg.ctx['x39'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y39'] = 'Saidas de Biguacu de segunda a sexta:'
        msg.ctx['z39'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w39'] = 'Saidas de Biguacu de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta64300(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x39'] + """
16:40  Tijucas - Timbe - Sorocaba dentro - Cadeado
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBiguacuSegundaaSexta64300(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y39'] + """
05:30 Saida Madereira - Sorocaba Dentro - Timbe - Tijucas
12:10 Viad Janaina - FAZDENTRO - SPRPCDENTRO -Timbe
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados64300(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z39'] + """
Sabados:
11:00 Tijucas - Timbe- Sorocaba Dentro - Viaduto Janaina"""

        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBiguacuSabadosDomingoseFeriados64300(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w39'] + """
Sabados:
07:30 Saida Furacao- Sorocaba Dentro - Timbe - Tijucas
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Sorocaba(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Sorocaba

/rota_Sorocaba"""

    @botcmd
    def horario_Sorocaba(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta64200
/SaidasCentroSegundaaSexta64200
/SaidasBairroSabadosDomingoseFeriados64200
/SaidasCentroSabadosDomingoseFeriados64200"""
        msg.ctx['x40'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y40'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z40'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w40'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta64200(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x40'] + """
06:22 Saida Timbe - Sorocaba Dentro
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta64200(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y40'] + """
17:10 Sorocaba Dentro - Timbe - Cadeado
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados64200(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z40'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados64200(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
           yield msg.ctx['w40'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Sorocaba_Viaduto_Janaina(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Sorocaba_Viaduto_Janaina

/rota_Sorocaba_Viaduto_Janaina"""

    @botcmd
    def horario_Sorocaba_Viaduto_Janaina(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta64201
/SaidasBiguacuSegundaaSexta64201
/SaidasBairroSabadosDomingoseFeriados64201
/SaidasBiguacuSabadosDomingoseFeriados64201"""
        msg.ctx['x41'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y41'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z41'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w41'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta64201(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x41'] + """
04:50 Saida Canto Bepao
06:22 
12:10 Timbe - Mercado Melo - Sorocaba Dentro - Canto Bepao
16:50 Sorocaba Dentro
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBiguacuSegundaaSexta64201(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y41'] + """
05:42 Furacao - Timbe - Sorocaba Dentro
11:10 Viaduto Janaina - Cadeado - Timbe - Macanganha
15:45 Entra Fazenda Dentro
17:41 Viaduto Janaina - Sorocaba Dentro - Timbe - Cadeado
19:00 Viaduto Janaina - Sorocaba Dentro - Timbe - Cadeado
22:35
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados64201(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z41'] + """
Sabados:
06:30 Saida Sorocaba dentro - BEPAO - Viaduto Janaina
Domingos e Feriados:
18:00 Timbe - Sorocaba - Canto Bepao - Viaduto Janaina
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBiguacuSabadosDomingoseFeriados64201(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w41'] + """
Sabados:
12:40 Viaduto Janaina _ Bepao - Sorocaba Dentro
Domingos e Feriados:
17:10 Viaduto Janaina - Canto BEPAO - Sorocaba - Timbe
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Shopping_Center_Itaguacu(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Shopping_Center_Itaguacu

/rota_Shopping_Center_Itaguacu"""

    @botcmd
    def horario_Shopping_Center_Itaguacu(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta12400
/SaidasCentroSegundaaSexta12400
/SaidasBairroSabadosDomingoseFeriados12400
/SaidasCentroSabadosDomingoseFeriados12400"""
        msg.ctx['x42'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y42'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z42'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w42'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta12400(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x42'] + """
06:10
06:35
06:55
07:20
07:40
08:05
08:30
09:00
09:30
10:05
10:40
11:20
11:55
12:30
13:00
13:30
14:00 Onibus Articulado
14:30
15:00
15:35 Onibus Articulado
16:10
16:45
17:10
17:30
17:55
18:05
18:35
18:59
19:15
19:35
20:05
20:50
21:25
22:00
22:30
22:55
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta12400(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y42'] + """
06:30
07:15
07:40
08:00
08:30
09:05
09:40
10:15
10:50
11:25
12:00
12:30
13:00
13:30 Onibus Articulado
14:00
14:35
15:10 Onibus Articulado
15:45
16:15
16:45
16:55
17:25
17:55
18:20
18:45
19:10
19:40
20:20
21:00
21:30
22:00
22:30
23:00
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados12400(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z42'] + """
Sabados:
06:10
06:45
07:10
07:30
07:50
08:10
08:35
09:00
09:30
10:00
10:30
11:00
11:30
12:00
12:30
13:00
13:30
14:00
14:30
15:10
15:50
16:25
17:10
17:50
18:30
19:10
20:00
20:45
21:40
22:30
Domingos e Feirados:
06:10
07:20
08:30
09:26
10:30
11:34
12:38
13:42
14:35
15:25
16:15
17:05
17:55
18:45
19:35
20:25
21:15
22:05
22:45
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados12400(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w42'] + """
Sabados:
06:45
07:20
07:45
08:05
08:30
09:00
09:30
10:00
10:30
11:00
11:30
12:00
12:30
13:00
13:30
14:00
14:40
15:20
16:00
16:40
17:20
18:00
18:40
19:30
20:20
21:10
22:00
23:00

Domingos e Feriados:
06:55
08:05
09:01
10:05
11:09
12:13
13:17
14:10
15:00
15:50
16:40
17:30
18:20
19:10
20:00
20:50
21:40
22:20
23:00
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Saudade(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Saudade

/rota_Saudade"""

    @botcmd
    def horario_Saudade(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta44303
/SaidasCentroSegundaaSexta44303
/SaidasBairroSabadosDomingoseFeriados44303
/SaidasCentroSabadosDomingoseFeriados44303"""
        msg.ctx['x43'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y43'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z43'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w43'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta44303(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x43'] + """
05:35 Onibus Articulado
06:00
06:10 Sai Faz Dentro e  Simplicio
06:50
08:05
10:00 Onibus Adaptado
12:30 Saida Entrada da Granja
13:55
15:35
17:00
17:40
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta44303(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y43'] + """
09:10 Adaptado
11:30 Ate Entrada da Granja
13:00
14:35
16:00
16:35
18:00
18:40
19:15
20:35
22:45
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados44303(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z43'] + """
Sabados:
05:50
06:40
13:15
17:45

Domingos e Feriados:
05:50
07:00
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados44303(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w43'] + """
Sabados:
12:20
16:50
18:05
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[Ss].*o.*[Mm]iguel")
    def Sao_Miguel(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Sao_Miguel

/rota_Sao_Miguel"""

    @botcmd
    def horario_Sao_Miguel(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasEstivaSegundaaSexta10900
/SaidasCentroSegundaaSexta10900
/SaidasEstivaSabadosDomingoseFeriados10900
/SaidasCentroSabadosDomingoseFeriados10900"""
        msg.ctx['x44'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y44'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z44'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w44'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasEstivaSegundaaSexta10900(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x44'] + """
05:25 Saida Loteamento Carolina
05:50
06:50 Passa Lot Carolina
12:40
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta10900(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y44'] + """
11:30
14:50 Via BR101 - Viaduto Palmas - Madereira Josiane
17:35 Via Cachoeria
18:30
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasEstivaSabadosDomingoseFeriados10900(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z44'] + """
Sabados:
06:45
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados10900(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w44'] + """
Sabados:
12:10"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[Ss]anta.*[Mm]aria.*[Aa]nt.*$")
    def Santa_Maria_Antonio_Carlos(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Santa_Maria_Antonio_Carlos

/rota_Santa_Maria_Antonio_Carlos"""

    @botcmd
    def horario_Santa_Maria_Antonio_Carlos(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta960000
/SaidasCentroSegundaaSexta960000
/SaidasBairroSabadosDomingoseFeriados960000
/SaidasCentroSabadosDomingoseFeriados960000"""
        msg.ctx['x45'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y45'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z45'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w45'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta960000(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x45'] + """
07:30 Rodoviaria - S Maria - Rodoviaria
17:35
19:51
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta960000(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y45'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados960000(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z45'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados960000(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w45'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

#==========================================================Imperatriz===============================================================================
#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Alto_Aririu_Florianopolis(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Alto_Aririu_Florianopolis

/rota_Alto_Aririu_Florianopolis"""

    @botcmd
    def horario_Alto_Aririu_Florianopolis(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta6281
/SaidasCentroSegundaaSexta6281
/SaidasBairroSabadosDomingoseFeriados6281
/SaidasCentroSabadosDomingoseFeriados6281"""
        msg.ctx['x46'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y46'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z46'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w46'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta6281(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x46'] + """
|06:20|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta6281(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y46'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados6281(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z46'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados6281(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w46'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Capela_Alto_Aririu_Florianopolis(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Capela_Alto_Aririu_Florianopolis

/rota_Capela_Alto_Aririu_Florianopolis"""

    @botcmd
    def horario_Capela_Alto_Aririu_Florianopolis(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta6283
/SaidasCentroSegundaaSexta6283
/SaidasBairroSabadosDomingoseFeriados6283
/SaidasCentroSabadosDomingoseFeriados6283"""
        msg.ctx['x47'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y47'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z47'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w47'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta6283(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x47'] + """
06:00
07:00
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta6283(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y47'] + """
17:05"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados6283(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z47'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados6283(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w47'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Aririu_Caldas_Imperatriz(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Aririu_Caldas_Imperatriz

/rota_Aririu_Caldas_Imperatriz"""

    @botcmd
    def horario_Aririu_Caldas_Imperatriz(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta681
/SaidasCentroSegundaaSexta681
/SaidasBairroSabadosDomingoseFeriados681
/SaidasCentroSabadosDomingoseFeriados681"""
        msg.ctx['x48'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y48'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z48'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w48'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta681(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x48'] + """
05:55
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta681(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y48'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados681(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z48'] + """
Sabados:
|05:50|
Domingos e Feriados:
|05:50|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados681(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w48'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Aguas_Mornas_Florianopolis(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Aguas_Mornas_Florianopolis

/rota_Aguas_Mornas_Florianopolis"""

    @botcmd
    def horario_Aguas_Mornas_Florianopolis(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta6240
/SaidasCentroSegundaaSexta6240
/SaidasBairroSabadosDomingoseFeriados6240
/SaidasCentroSabadosDomingoseFeriados6240"""
        msg.ctx['x49'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y49'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z49'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w49'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta6240(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x49'] + """
|05:55|
|09:40|
|10:15|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta6240(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y49'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados6240(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z49'] + """
Sabados:
|05:35|
|10:20|
|15:40|

Domingos e Feriados:
|06:25|
|15:50|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados6240(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w49'] + """
Sabados:
|08:40|
|14:20|
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Capela_Alto_Aririu_Florianopolis_Rod_Municipais(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Capela_Alto_Aririu_Florianopolis_Rod_Municipais

/rota_Capela_Alto_Aririu_Florianopolis_Rod_Municipais"""


    @botcmd
    def horario_Capela_Alto_Aririu_Florianopolis_Rod_Municipais(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta6282
/SaidasCentroSegundaaSexta6282
/SaidasBairroSabadosDomingoseFeriados6282
/SaidasCentroSabadosDomingoseFeriados6282"""
        msg.ctx['x50'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y50'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z50'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w50'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta6282(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x50'] + """
|06:00|
|07:10|
Via Capela, Rod. Municipais e Estaduais
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta6282(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y50'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados6282(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z50'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados6282(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w50'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Florianopolis_Caldas_da_Imperatriz(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Florianopolis_Caldas_da_Imperatriz

/rota_Florianopolis_Caldas_da_Imperatriz"""

    @botcmd
    def horario_Florianopolis_Caldas_da_Imperatriz(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta680
/SaidasCentroSegundaaSexta680
/SaidasBairroSabadosDomingoseFeriados680
/SaidasCentroSabadosDomingoseFeriados680"""
        msg.ctx['x51'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y51'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z51'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w51'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta680(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x51'] + """
|05:00|
|06:00|
|08:00|
|10:45|
|13:45|
|15:30|
|17:40|
|19:15|
|21:15|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta680(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y51'] + """
|09:00|
|12:10|
|13:30|
|19:40|
|20:40|
|22:20|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados680(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z51'] + """
Sabados:
08:15
11:10
13:30
13:45
18:00
21:20
Domingos e Feriados:
07:50
11:25
14:00
19:00
21:30
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados680(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w51'] + """
Sabados:
|09:10|
|16:20|
|20:20|
|21:50|
Domingos e Feriados:
|09:40|
|12:20|
|17:00|
|20:20|
|22:00|
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------

    @botcmd
    def Florianopolis_Caldas_da_Imperatriz_SF_BR(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Florianopolis_Caldas_da_Imperatriz_SF_BR

/rota_Florianopolis_Caldas_da_Imperatriz_Via_SF_BR"""

    @botcmd
    def horario_Florianopolis_Caldas_da_Imperatriz_SF_BR(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta6823
/SaidasCentroSegundaaSexta6823
/SaidasBairroSabadosDomingoseFeriados6823
/SaidasCentroSabadosDomingoseFeriados6823"""
        msg.ctx['x52'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y52'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z52'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w52'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta6823(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x52'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta6823(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y52'] + """
Via Bairro Sao Francisco:
|16:25|
|18:35|

Via BR-101 e BR-282:
|16:00|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados6823(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z52'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados6823(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w52'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Lourdes2_Florianopolis(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Lourdes2_Florianopolis

/rota_Lourdes2_Florianopolis"""

    @botcmd
    def horario_Lourdes2_Florianopolis(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta970
/SaidasCentroSegundaaSexta970
/SaidasBairroSabadosDomingoseFeriados970
/SaidasCentroSabadosDomingoseFeriados970"""
        msg.ctx['x53'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y53'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z53'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w53'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta970(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x53'] + """
|05:45|
|06:40|
|12:15|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta970(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y53'] + """
|10:20|
|16:55|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados970(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z53'] + """
Sabados:
|06:50|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados970(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w53'] + """
Sabados:
|12:00|
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Lourdes2_SA_Imperatriz(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Lourdes2_SA_Imperatriz

/rota_Lourdes2_SA_Imperatriz"""

    @botcmd
    def horario_Lourdes2_SA_Imperatriz(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta6290
/SaidasCentroSegundaaSexta6290
/SaidasBairroSabadosDomingoseFeriados6290
/SaidasCentroSabadosDomingoseFeriados6290"""
        msg.ctx['x54'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y54'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z54'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w54'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta6290(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x54'] + """
|17:10|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta6290(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y54'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados6290(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z54'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados6290(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w54'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @re_botcmd(pattern=r"^[Qq]ue.*b.*")
    def Quecaba(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Quecaba

/rota_Quecaba"""

    @botcmd
    def horario_Quecaba(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta660
/SaidasCentroSegundaaSexta660
/SaidasBairroSabadosDomingoseFeriados660
/SaidasCentroSabadosDomingoseFeriados660"""
        msg.ctx['x55'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y55'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z55'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w55'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta660(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x55'] + """
|05:20|
|12:40|
|18:10|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta660(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y55'] + """
|09:30|
|15:50|
|16:40|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados660(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z55'] + """
Sabados:
|06:20|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados660(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w55'] + """
Sabados:
|13:00|"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def SA_Imperatriz_Florianopolis670(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_SA_Imperatriz_Florianopolis670

/rota_SA_Imperatriz_Florianopolis670"""

    @botcmd
    def horario_SA_Imperatriz_Florianopolis670(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta670
/SaidasCentroSegundaaSexta670
/SaidasBairroSabadosDomingoseFeriados670
/SaidasCentroSabadosDomingoseFeriados670"""
        msg.ctx['x56'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y56'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z56'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w56'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta670(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x56'] + """
|04:50|
|09:30|
|11:20|
|15:00|
|16:20|
|20:30|
|22:20|
Via:BR282, Rodovias Municipais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta670(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y56'] + """
|06:25|
|07:00|
|08:00|
|12:40|
|14:50|
|15:30|
|16:10|
|17:30|
|23:15|
Via:BR282, Rodovias Municipais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados670(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z56'] + """
Sabados:
|05:20|
|06:20|
|10:10|
|12:10|
|15:20|
|16:40|
|17:30|
|19:50|
|20:40|
Domingos e Feriados:
|05:30|
|09:20|
|13:00|
|15:10|
|18:10|
Via:BR282, Rodovias Municipais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados670(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w56'] + """
Sabados:
|07:20|
|08:00|
|10:20|
|10:50|
|12:30|
|17:40|
|18:20|
|19:00|
|19:40|
|21:00|
|22:40|

Domingos e Feriados:
|08:00|
|10:00|
|11:00|
|18:20|
|19:20|
|21:00|
|22:50|
Via:BR282, Rodovias Municipais"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def SA_Imperatriz_Florianopolis6271(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_SA_Imperatriz_Florianopolis6271

/rota_SA_Imperatriz_Florianopolis6271"""

    @botcmd
    def horario_SA_Imperatriz_Florianopolis6271(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta6271
/SaidasCentroSegundaaSexta6271
/SaidasBairroSabadosDomingoseFeriados6271
/SaidasCentroSabadosDomingoseFeriados6271"""
        msg.ctx['x57'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y57'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z57'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w57'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta6271(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x57'] + """
|05:30|
|06:20|
|12:30|
|16:40|
Via Sertão, Reta dos Pilões e Rod. Municipais
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta6271(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y57'] + """
|07:30|
|11:20|
|17:50|
|19:20|
Via Sertão, Reta dos Pilões e Rod. Municipais
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados6271(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z57'] + """
Sabados:
|07:10|
Via Sertão, Reta dos Pilões e Rod. Municipais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados6271(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w57'] + """
Sabados:
|13:40|
Via Sertão, Reta dos Pilões e Rod. Municipais"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def SA_Imperatriz_Florianopolis6270(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_SA_Imperatriz_Florianopolis6270

/rota_SA_Imperatriz_FLorianopolis6270"""

    @botcmd
    def horario_SA_Imperatriz_Florianopolis6270(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta6270
/SaidasCentroSegundaaSexta6270
/SaidasBairroSabadosDomingoseFeriados6270
/SaidasCentroSabadosDomingoseFeriados6270"""
        msg.ctx['x58'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y58'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z58'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w58'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta6270(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x58'] + """
|05:15|
|05:55|
|06:30|
|07:30|
|08:40|
|12:00|
|15:30|
|17:10|
Via Sul do Rio / Rodovias Municipais
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta6270(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y58'] + """
|06:45|
|10:40|
|13:10|
|14:30|
|17:10|
|19:00|
Via Sul do Rio / Rodovias Municipais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados6270(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z58'] + """
Sabados:
|06:40|
|09:00|
Via Sul do Rio / Rodovias Municipais"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados6270(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w58'] + """
Sabados:
|15:00|
Via Sul do Rio / Rodovias Municipais"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def SA_Imperatriz_Florianopolis6261(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_SA_Imperatriz_Florianopolis6261

/rota_SA_Imperatriz_Florianopolis6261"""

    @botcmd
    def horario_SA_Imperatriz_Florianopolis6261(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta6261
/SaidasCentroSegundaaSexta6261
/SaidasBairroSabadosDomingoseFeriados6261
/SaidasCentroSabadosDomingoseFeriados6261"""
        msg.ctx['x59'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y59'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z59'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w59'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta6261(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x59'] + """
|05:50|
|06:40|
|07:15|
|11:55|
|16:50|
|17:25| Linha 626 2
|18:00|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta6261(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y59'] + """
|12:20|
|14:00|
|15:35|
|16:30|
|18:00|
|18:30|
|19:10|
|19:40|
|20:20|
|22:30|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados6261(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z59'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados6261(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w59'] + """
Sabados:
|12:40|"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def SA_Imperatriz_Florianopolis6260(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_SA_Imperatriz_Florianopolis6260


/rota_SA_Imperatriz_Florianopolis6260"""

    @botcmd
    def horario_SA_Imperatriz_Florianopolis6260(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta6260
/SaidasCentroSegundaaSexta6260
/SaidasBairroSabadosDomingoseFeriados6260
/SaidasCentroSabadosDomingoseFeriados6260"""
        msg.ctx['x60'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y60'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z60'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w60'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta6260(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x60'] + """
|06:00|
|07:00|
|12:05|
Via:BR-282, BR-101 Marginal e Via Expressa"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta6260(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y60'] + """
|16:50|
|17:10|
|17:50|
|18:50|
Via:BR-282, BR-101 Marginal e Via Expressa"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados6260(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z60'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados6260(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w60'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def SA_Imperatriz_Florianopolis671(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_SA_Imperatriz_Florianopolis671

/rota_SA_Imperatriz_Florianopolis671"""

    @botcmd
    def horario_SA_Imperatriz_Florianopolis671(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta671
/SaidasCentroSegundaaSexta671
/SaidasBairroSabadosDomingoseFeriados671
/SaidasCentroSabadosDomingoseFeriados671"""
        msg.ctx['x61'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y61'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z61'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w61'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta671(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x61'] + """
|05:30|
|05:50|
|06:30|
|12:10|
Via B. Sao Francisco/BR 282"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta671(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y61'] + """
|11:40|
Via B. Sao Francisco/BR 282"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados671(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z61'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados671(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w61'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Santa_Isabel_Florianopolis(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Santa_Isabel_Florianopolis

/rota_Santa_Isabel_Florianopolis"""

    @botcmd
    def horario_Santa_Isabel_Florianopolis(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta830
/SaidasCentroSegundaaSexta830
/SaidasBairroSabadosDomingoseFeriados830
/SaidasCentroSabadosDomingoseFeriados830"""
        msg.ctx['x62'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y62'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z62'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w62'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta830(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x62'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""

        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta830(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y62'] + """
|11:10|
|15:10|
|18:10|
"""

        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados830(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z62'] + """
Sabados:
|07:10|
|13:40|
|18:00|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados830(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w62'] + """
Sabados:
|11:20|
|15:40|
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Vargem_Grande_2_Florianopolis(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Vargem_Grande_2_Florianopolis

/rota_Vargem_Grande_2_Florianopolis"""

    @botcmd
    def horario_Vargem_Grande_2_Florianopolis(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta6250
/SaidasCentroSegundaaSexta6250
/SaidasBairroSabadosDomingoseFeriados6250
/SaidasCentroSabadosDomingoseFeriados6250"""
        msg.ctx['x63'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y63'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z63'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w63'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta6250(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x63'] + """
|05:15|Via BR282 Rodovias Municipais
|06:25|Via BR282 Rodovias Municipais
|08:20|Via BR282 Rodovias Municipais
|11:15|Via BR282 Rodovias Municipais
|12:00|Via BR-282 BR-101 e Via Expressa
|16:20|Via BR282 Rodovias Municipais
|17:00|Via BR282 Rodovias Municipais
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta6250(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y63'] + """
|06:00|Via BR282 Rodovias Municipais
|08:30|Via BR282 Rodovias Municipais
|10:00|Via BR282 Rodovias Municipais
|13:50|Via BR282 Rodovias Municipais
|14:10|Via BR282 Rodovias Municipais
|17:40|Via BR-282 BR-101 e Via Expressa
|20:00|Via BR282 Rodovias Municipais
|21:30|Via BR282 Rodovias Municipais
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados6250(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z63'] + """
Sabados:
|09:00|Via BR282 Rodovias Municipais
|12:20|Via BR282 Rodovias Municipais

Domingos e Feriados:
|09:45|Via BR282 Rodovias Municipais
|16:50|Via BR282 Rodovias Municipais
|19:40|Via BR282 Rodovias Municipais

"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados6250(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w63'] + """
Sabados:
|06:40|Via BR282 Rodovias Municipais
|09:50|Via BR282 Rodovias Municipais
|17:00|Via BR282 Rodovias Municipais

Domingos e Feriados:
|07:00|Via BR282 Rodovias Municipais
|13:20|Via BR282 Rodovias Municipais
|15:40|Via BR282 Rodovias Municipais

"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Bairro_Sao_Luiz143(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Bairro_Sao_Luiz143

/rota_Bairro_Sao_Luiz143"""

    @botcmd
    def horario_Bairro_Sao_Luiz143(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta143
/SaidasCentroSegundaaSexta143
/SaidasBairroSabadosDomingoseFeriadosi143
/SaidasCentroSabadosDomingoseFeriados143"""
        msg.ctx['x64'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y64'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z64'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w64'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta143(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x64'] + """
|06:10| 
|07:10| 
|11:00| 
|13:00| 
|16:00| 
|18:12|
|22:05| Shopping Cont.
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta143(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y64'] + """
|10:33| 
|12:30| 
|15:30| 
|17:35| 
|19:33| 
|21:43| 
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados143(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z64'] + """
Sabados:
|07:00|
|17:00|
|19:00| 

Domingos e Feriados:
|17:00| 
|19:15| 
    
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados143(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w64'] + """
Sabados:
|16:30|
|18:30|
Domingos e Feriados:
|16:35|
|18:45|
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Forquilhas08(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Forquilhas08

/rota_Forquilhas08"""

    @botcmd
    def horario_Forquilhas08(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta08
/SaidasCentroSegundaaSexta08
/SaidasBairroSabadosDomingoseFeriados08
/SaidasCentroSabadosDomingoseFeriados08"""
        msg.ctx['x65'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y65'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z65'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w65'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta08(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x65'] + """
|05:45| 
|12:50| """
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta08(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y65'] + """
|12:05| P.Baixo
|18:15| P.Baixo 
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados08(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z65'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados08(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w65'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Irineu_Comelli(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Irineu_Comelli

/rota_Irineu_Comelli"""

    @botcmd
    def horario_Irineu_Comelli(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta676
/SaidasCentroSegundaaSexta676
/SaidasBairroSabadosDomingoseFeriados676
/SaidasCentroSabadosDomingoseFeriados676"""
        msg.ctx['x66'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y66'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z66'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w66'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta676(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x66'] + """
|05:30| 
|05:50|  P.Comprida
|06:51|  P.Comprida
|13:05|  P.Comprida"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta676(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y66'] + """
|12:15| """
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados676(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z66'] + """
|06:10|  P.Comprida
|07:35|  P.Comprida """
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados676(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w66'] + """
Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
-> /empresas"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Hospital_Regional(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Hospital_Regional

/rota_Hospital_Regional"""

    @botcmd
    def horario_Hospital_Regional(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta202
/SaidasCentroSegundaaSexta202
/SaidasBairroSabadosDomingoseFeriados202
/SaidasCentroSabadosDomingoseFeriados202"""
        msg.ctx['x67'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y67'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z67'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w67'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta202(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x67'] + """
|06:00| Saída da IFSC
|06:30|
|07:00| Saída da IFSC
|07:20|
|07:50|
|08:30|
|09:00|
|09:40|
|10:20|
|10:53|
|11:25|
|11:55|
|12:25|
|12:54|
|13:14| Saída da IFSC
|13:45| Via Expressa
|14:15|
|14:45|
|15:25|
|15:55|
|16:12|
|16:30|
|16:55|
|17:25|
|18:05|
|18:30|
|19:25|
|20:00|
|20:25|
|20:53|
|21:15| 
|22:10|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta202(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y67'] + """
|06:30|
|06:55|
|07:25|
|08:05|
|09:20|
|10:00|
|10:30|
|11:00|
|11:30|
|12:05|
|12:30|
|12:50|
|13:20|
|13:50|
|14:20|
|15:00|
|15:30|
|16:00|
|16:30|
|16:55|
|17:30|
|18:00|
|18:25| I.Comelli
|18:55|
|19:30| I.Comelli
|20:05|
|20:30|
|21:03|
|21:40|
|22:15|
|22:50|"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados202(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z67'] + """
Sabados:
|06:15| Saída da IFSC
|07:00|
|07:40| Saída da IFSC
|08:40|
|09:40|
|10:30|
|11:45|
|15:00|
|15:55|
|17:10|
|18:40|
|19:30|
"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados202(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w67'] + """
Sabados:
|06:40|
|07:25|
|08:20|
|09:15|
|10:05|
|11:20|
|12:40| I.Comelli
|13:40|
|15:30|
|16:35|
|18:15|
|19:05|
"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botcmd
    def Ponta_de_Baixo(self, msg, args):
        yield """Ola, o que deseja saber?
/horario_Ponta_de_Baixo

/rota_Ponta_de_Baixo"""

    @botcmd
    def horario_Ponta_de_Baixo(self, msg, args):
        """Linha do Onibus"""
        yield """Qual saida?
/SaidasBairroSegundaaSexta203
/SaidasCentroSegundaaSexta203
/SaidasBairroSabadosDomingoseFeriados203
/SaidasCentroSabadosDomingoseFeriados203"""
        msg.ctx['x68'] = 'Saidas do bairro de segunda a sexta:'
        msg.ctx['y68'] = 'Saidas do centro de segunda a sexta:'
        msg.ctx['z68'] = 'Saidas do bairro de sabados, domingos e feriados:'
        msg.ctx['w68'] = 'Saidas do centro de sabados, domingos e feriados:'

    @botcmd
    def SaidasBairroSegundaaSexta203(self, msg, args, flow_only=True):
        """Saidas do bairro de segunda a sexta"""
        try:
            yield msg.ctx['x68'] + """
 06:00 1 Saída da IFSC
 06:30 1
 07:00 1 Saída da IFSC
 07:20 1
 07:50 1
 08:30 1
 09:00 1
 09:40 1
 10:20 1
 10:53 1
 11:25 1
 11:55 1
 12:25 1
 12:54 1
 13:14 1 Saída da IFSC
 13:45 2 Via Expressa
 14:15 1
 14:45 1
 15:25 1
 15:55 1
 16:12 1
 16:30 1
 16:55 1
 17:25 1
 18:05 1
 18:30 1
 19:25 1
 20:00 1
 20:25 1
 20:53 1
 21:15 1
 22:10 1"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSegundaaSexta203(self, msg, args, flow_only=True):
        """Saidas do centro de segunda a sexta"""
        try:
            yield msg.ctx['y68'] + """
 06:30 1
 06:55 1
 07:25 1
 08:05 1
 09:20 1
 10:00 1
 10:30 1
 11:00 1
 11:30 1
 12:05 1
 12:30 1
 12:50 1
 13:20 1
 13:50 1
 14:20 1
 15:00 1
 15:30 1
 16:00 1
 16:30 1
 16:55 1
 17:30 1
 18:00 1
 18:25 1 I.Comelli
 18:55 1
 19:30 1 I.Comelli
 20:05 1
 20:30 1
 21:03 1
 21:40 1
 22:15 1
 22:50 1"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasBairroSabadosDomingoseFeriados203(self, msg, args, flow_only=True):
        """Saidas do bairro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['z68'] + """
Sabados:
 06:15 1 Saída da IFSC
 07:00 1
 07:40 1 Saída da IFSC
 08:40 1
 09:40 1
 10:30 1
 11:45 1
 15:00 1
 15:55 1
 17:10 1
 18:40 1
 19:30 1"""
        except:
            yield "Primeiro informe a linha que deseja"

    @botcmd
    def SaidasCentroSabadosDomingoseFeriados203(self, msg, args, flow_only=True):
        """Saidas do centro de sabados, domingos e feriados"""
        try:
            yield msg.ctx['w68'] + """
Sabados:
 06:40 1
 07:25 1
 08:20 1
 09:15 1
 10:05 1
 11:20 1
 12:40 1 I.Comelli
 13:40 1
 15:30 1
 16:35 1
 18:15 1
 19:05 1"""
        except:
            yield "Primeiro informe a linha que deseja"


#----------------------------------------------------------------------------------------------------------------------------------------------------
#    @botcmd
#    def linha_do_onibus(self, msg, args):
#        yield """Ola, o que deseja saber?
#/horario_linha_do_onibus
#
#/rota_linha_do_onibus"""
#
#    @botcmd
#    def horario_linha_do_onibus(self, msg, args):
#        """Linha do Onibus"""
#        yield """Qual saida?
#/SaidasBairroSegundaaSexta
#/SaidasCentroSegundaaSexta
#/SaidasBairroSabadosDomingoseFeriados
#/SaidasCentroSabadosDomingoseFeriados"""
#        msg.ctx['x.'] = 'Saidas do bairro de segunda a sexta:'
#        msg.ctx['y.'] = 'Saidas do centro de segunda a sexta:'
#        msg.ctx['z.'] = 'Saidas do bairro de sabados, domingos e feriados:'
#        msg.ctx['w.'] = 'Saidas do centro de sabados, domingos e feriados:'
#
#    @botcmd
#    def SaidasBairroSegundaaSexta(self, msg, args, flow_only=True):
#        """Saidas do bairro de segunda a sexta"""
#        try:
#            yield msg.ctx['x.'] + """horario"""
#        except:
#            yield "Primeiro informe a linha que deseja"
#
#    @botcmd
#    def SaidasCentroSegundaaSexta(self, msg, args, flow_only=True):
#        """Saidas do centro de segunda a sexta"""
#        try:
#            yield msg.ctx['y.'] + """horario"""
#        except:
#            yield "Primeiro informe a linha que deseja"
#
#    @botcmd
#    def SaidasBairroSabadosDomingoseFeriados(self, msg, args, flow_only=True):
#        """Saidas do bairro de sabados, domingos e feriados"""
#        try:
#            yield msg.ctx['z.'] + """
#Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
#-> /empresas"""
#        except:
#            yield "Primeiro informe a linha que deseja"
#
#    @botcmd
#    def SaidasCentroSabadosDomingoseFeriados(self, msg, args, flow_only=True):
#        """Saidas do centro de sabados, domingos e feriados"""
#        try:
#            yield msg.ctx['w.'] + """
#Esse onibus nao possui horario nesses dias, deseja consultar as empresas?
#-> /empresas"""
#        except:
#            yield "Primeiro informe a linha que deseja"
#
#
#----------------------------------------------------------------------------------------------------------------------------------------------------
