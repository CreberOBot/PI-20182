from errbot import botflow, FlowRoot, BotFlow

class BuzauFlow(BotFlow):
    """Perdidos na cidade"""
#----------------------------------------------------------------------------------------------------------------------------------------------------
#FLOWGENERICO FAVOR NAO MEXER PARA NAO DEIXAR O PROGRAMADOR PUTO!!!!!!
#    @botflow
#    def linhadoonibus(self, flow: FlowRoot):
#        """Linha do Onibus"""
#        step1 = flow.connect('horario_linha_do_onibus', auto_trigger=True)
#        step2 = step1.connect('SaidasBairroSegundaaSexta')
#        step3 = step1.connect('SaidasCentroSegundaaSexta')
#        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados')
#        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados')
#
#----------------------------------------------------------------------------------------------------------------------------------------------------
#================================================Santa Terezinha===========================================================
    @botflow
    def JardimPinheirosKobrasol(self, flow: FlowRoot):
        """Jardim Pinheiros Kobrasol"""
        step1 = flow.connect('horario_Jardim_Pinheiros_Kobrasol', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta0900')
        step3 = step1.connect('SaidasCentroSegundaaSexta0900')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados0900')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados0900')

    @botflow
    def ContinenteParkShoppingFlorianopolis(self, flow: FlowRoot):
        """Continente Park Shopping Florianopolis"""
        step1 = flow.connect('horario_Continente_Park_Shopping_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSextaSN')
        step3 = step1.connect('SaidasCentroSegundaaSextaSN')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriadosSN')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriadosSN')

    @botflow
    def CoqueirosAngelinaBetaniaeRanchoQueimado(self, flow: FlowRoot):
        """Coqueiros Angelina Betania e Rancho Queimado"""
        step1 = flow.connect('horario_Coqueiros_Angelina_Betania_e_Rancho_Queimado', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta553')
        step3 = step1.connect('SaidasCentroSegundaaSexta553')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados553')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados553')

    @botflow
    def FlordeNapolisSantoAndre(self, flow: FlowRoot):
        """Flor de Napolis Santo Andre"""
        step1 = flow.connect('horario_Flor_de_Napolis_Santo_Andre', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta175')
        step3 = step1.connect('SaidasCentroSegundaaSexta175')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados175')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados175')

    @botflow
    def SantanaFlorianopolis(self, flow: FlowRoot):
        """Santana Florianopolis"""
        step1 = flow.connect('horario_Santana_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta178')
        step3 = step1.connect('SaidasCentroSegundaaSexta178')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados178')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados178')

    @botflow
    def SantanaKobrasol(self, flow: FlowRoot):
        """Santana Kobrasol"""
        step1 = flow.connect('horario_Santana_Kobrasol', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta901')
        step3 = step1.connect('SaidasCentroSegundaaSexta901')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados901')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados901')

    @botflow
    def SaoPedrodeAlcantraFlorianopolis(self, flow: FlowRoot):
        """SaoPedrodeAlcantraFlorianopolis"""
        step1 = flow.connect('horario_Sao_Pedro_de_Alcantra_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta177')
        step3 = step1.connect('SaidasCentroSegundaaSexta177')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados177')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados177')

    @botflow
    def Sertao_do_Maruim_Florianopolis(self, flow: FlowRoot):
        """Sertao do Maruim Florianopolis"""
        step1 = flow.connect('horario_Sertao_do_Maruim_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta554')
        step3 = step1.connect('SaidasCentroSegundaaSexta554')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados554')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados554')

    @botflow
    def Vila_Formosa_Florianopolis(self, flow: FlowRoot):
        """Vila Formosa Florianopolis"""
        step1 = flow.connect('horario_Vila_Formosa_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta5541')
        step3 = step1.connect('SaidasCentroSegundaaSexta5541')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados5541')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados5541')
#----------------------------------------------------------------------------------------------------------------------------------------------------

#==================================estrela====================================

    @botflow
    def estrela(self, flow: FlowRoot):
        """Vamos ver se da"""
        step1 = flow.connect('estrela', auto_trigger=True)
        step2 = step1.connect('EstrelaInterMunicipal')
        step3 = step1.connect('EstrelaMunicipal')

#----------------------------------------------------------------------------------------------------------------------------------------------------
#   
#    @botflow
#    def Estrela(self, flow: FlowRoot):
#        """Vamos ver se da2"""
#        step1 = flow.connect('Estrela', auto_trigger=True)
#        step2 = step1.connect('EstrelaIntermunicipal')
#        step3 = step1.connect('EstrelaMunicipal')
#
#----------------------------------------------------------------------------------------------------------------------------------------------------

    @botflow
    def CH_Arthur_Mariano_Via_Ivo_silveira(self, flow: FlowRoot):
        """CH Arthur Mariano"""
        step1 = flow.connect('horario_CH_Arthur_Mariano_Circular_Forquilhinha', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta651')
        step3 = step1.connect('SaidasCentroSegundaaSexta651')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados651')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados651')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def CH_Forquilhinha(self, flow: FlowRoot):
        """Forquilhinhas"""
        step1 = flow.connect('horario_CH_Forquilhinha', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta117')
        step3 = step1.connect('SaidasCentroSegundaaSexta117')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados117')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados117')
         

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Campinas(self, flow: FlowRoot):
        """Campinas"""
        step1 = flow.connect('horario_Campinas', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta317')
        step3 = step1.connect('SaidasCentroSegundaaSexta317')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados317')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados317')
        

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Campinas_Via_Ginasio_de_Esportes(self, flow: FlowRoot):
        """Campinas Ginasio"""
        step1 = flow.connect('horario_Campinas_Via_Ginasio_de_Esportes', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta3171')
        step3 = step1.connect('SaidasCentroSegundaaSexta3171')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados3171')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados3171')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def CEASA_Via_Santos_Saraiva(self, flow: FlowRoot):
        """CEASA"""
        step1 = flow.connect('horario_CEASA_Via_Santos_Saraiva', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta328')
        step3 = step1.connect('SaidasCentroSegundaaSexta328')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados328')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados328')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Ceniro_Via_Jardim_das_Palmeiras(self, flow: FlowRoot):
        """Ceniro Jardim"""
        step1 = flow.connect('horario_Ceniro_Via_Jardim_das_Palmeiras', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta131')
        step3 = step1.connect('SaidasCentroSegundaaSexta131')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados131')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados131')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def D_Zenaide_Via_Santa_Felicidade_Ceniro(self, flow: FlowRoot):
        """Zenaide"""
        step1 = flow.connect('horario_D_Zenaide_Via_Santa_Felicidade_Ceniro', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta7632')
        step3 = step1.connect('SaidasCentroSegundaaSexta7632')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados7632')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados7632')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def EXECUTIVO_San_Marino_Lisboa(self, flow: FlowRoot):
        """EXECUTIVO San Marino Lisboa"""
        step1 = flow.connect('horario_EXECUTIVO_San_Marino_Lisboa', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta7633')
        step3 = step1.connect('SaidasCentroSegundaaSexta7633')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados7633')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados7633')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Forquilhas_Florianopolis(self, flow: FlowRoot):
        """Forquilhas Florianopolis"""
        step1 = flow.connect('horario_Forquilhas_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta0039')
        step3 = step1.connect('SaidasCentroSegundaaSexta0039')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados0039')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados0039')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Forquilhinha_Via_Rodeio_e_Palmares(self, flow: FlowRoot):
        """Forquilhinha Via Rodeio e Palmares"""
        step1 = flow.connect('horario_Forquilhinha_Via_Rodeio_e_Palmares', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta0392')
        step3 = step1.connect('SaidasCentroSegundaaSexta0392')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados0392')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados0392')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Kobrasol(self, flow: FlowRoot):
        """Kobrasol"""
        step1 = flow.connect('horario_Kobrasol', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta0141')
        step3 = step1.connect('SaidasCentroSegundaaSexta0141')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados0141')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados0141')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Kobrasol_VIP(self, flow: FlowRoot):
        """Kobrasol VIP"""
        step1 = flow.connect('horario_Kobrasol_VIP', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta1412')
        step3 = step1.connect('SaidasCentroSegundaaSexta1412')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados1412')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados1412')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Los_Angeles(self, flow: FlowRoot):
        """Los Angeles"""
        step1 = flow.connect('horario_Los_Angeles', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta763')
        step3 = step1.connect('SaidasCentroSegundaaSexta763')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados763')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados763')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Parque_Residencial_Lisboa(self, flow: FlowRoot):
        """Parque Residencial Lisboa"""
        step1 = flow.connect('horario_Parque_Residencial_Lisboa', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta7631')
        step3 = step1.connect('SaidasCentroSegundaaSexta7631')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados7631')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados7631')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Potecas(self, flow: FlowRoot):
        """Potecas"""
        step1 = flow.connect('horario_Potecas', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta0020')
        step3 = step1.connect('SaidasCentroSegundaaSexta0020')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados0020')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados0020')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Potecas_Santos_Saraiva(self, flow: FlowRoot):
        """Potecas Santos Saraiva"""
        step1 = flow.connect('horario_Potecas_Santos_Saraiva', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta0201')
        step3 = step1.connect('SaidasCentroSegundaaSexta0201')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados0201')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados0201')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Recanto_da_Natureza_Via_Ceniro_Martins(self, flow: FlowRoot):
        """Recanto da Natureza Via Ceniro Martins"""
        step1 = flow.connect('horario_Recanto_da_Natureza_Via_Ceniro_Martins', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta0202')
        step3 = step1.connect('SaidasCentroSegundaaSexta0202')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados0202')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados0202')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Bairro_Sao_luiz(self, flow: FlowRoot):
        """Bairro Sao Luiz"""
        step1 = flow.connect('horario_Bairro_Sao_Luiz', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta0142')
        step3 = step1.connect('SaidasCentroSegundaaSexta0142')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados0142')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados0142')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Serraria_Forquilhinha(self, flow: FlowRoot):
        """Serraria Forquilhinha"""
        step1 = flow.connect('horario_Serraria_Forquilhinhas', auto_trigger=True)
        step2 = step1.connect('SaidasSerrariaSegundaaSexta0105')
        step3 = step1.connect('SaidasForquilhinhasSegundaaSexta0105')
        step4 = step1.connect('SaidasSerrariaSabadosDomingoseFeriados0105')
        step5 = step1.connect('SaidasForquilhinhasSabadosDomingoseFeriados0105')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Barreiros_sede(self, flow: FlowRoot):
        """Barreiros sede"""
        step1 = flow.connect('horario_Barreiros_Sede', auto_trigger=True)
        step2 = step1.connect('SaidasBarreirosSegundaaSexta0110')
        step3 = step1.connect('SaidasSedeSegundaaSexta0110')
        step4 = step1.connect('SaidasBarreirosSabadosDomingoseFeriados0110')
        step5 = step1.connect('SaidasSedeSabadosDomingoseFeriados0110')

#----------------------------------------------------------------------------------------------------------------------------------------------------

    @botflow
    def Forquilhas_Kobrasol(self, flow: FlowRoot):
        """Forquilhas Kobrasol"""
        step1 = flow.connect('horario_Forquilhas_Kobrasol', auto_trigger=True)
        step2 = step1.connect('SaidasForquilhasSegundaaSexta0120')
        step3 = step1.connect('SaidasKobrasolSegundaaSexta0120')
        step4 = step1.connect('SaidasForquilhasSabadosDomingoseFeriados0120')
        step5 = step1.connect('SaidasKobrasolSabadosDomingoseFeriados0120')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Vila_Formosa(self, flow: FlowRoot):
        """Vila Formosa"""
        step1 = flow.connect('horario_Vila_Formosa', auto_trigger=True)
        step2 = step1.connect('SaidasVilaFormosaSegundaaSexta0125')
        step3 = step1.connect('SaidasKobrasolSegundaaSexta0125')
        step4 = step1.connect('SaidasVilaFormosaSabadosDomingoseFeriados0125')
        step5 = step1.connect('SaidasKobrasolSabadosDomingoseFeriados0125')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Diretao(self, flow: FlowRoot):
        """Diretao"""
        step1 = flow.connect('horario_Diretao', auto_trigger=True)
        step2 = step1.connect('SaidasBarreirosSegundaaSexta0130')
        step3 = step1.connect('SaidasFazendaSegundaaSexta0130')
        step4 = step1.connect('SaidasBarreirosSabadosDomingoseFeriados0130')
        step5 = step1.connect('SaidasFazendaSabadosDomingoseFeriados0130')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Potecas_Kobrasol(self, flow: FlowRoot):
        """Potecas Kobrasol"""
        step1 = flow.connect('horario_Potecas_Kobrasol', auto_trigger=True)
        step2 = step1.connect('SaidasPotecasSegundaaSexta0135')
        step3 = step1.connect('SaidasKobrasolSegundaaSexta0135')
        step4 = step1.connect('SaidasPotecasSabadosDomingoseFeriados0135')
        step5 = step1.connect('SaidasKobrasolSabadosDomingoseFeriados0135')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def EXECUTIVO_Diretao(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_EXECUTIVO_Diretao', auto_trigger=True)
        step2 = step1.connect('SaidasBarreirosSegundaaSexta0140')
        step3 = step1.connect('SaidasFazendaSegundaaSexta0140')
        step4 = step1.connect('SaidasBarreirosSabadosDomingoseFeriados0140')
        step5 = step1.connect('SaidasFazendaSabadosDomingoseFeriados0140')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Circular_Barreiros(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Circular_Barreiros', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta90900')
        step3 = step1.connect('SaidasBairroSabadosDomingoseFeriados90900')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Bom_Viver(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Bom_Viver', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta10000')
        step3 = step1.connect('SaidasCentroSegundaaSexta10000')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados10000')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados10000')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Tres_Riachos(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Tres_Riachos', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta44800')
        step3 = step1.connect('SaidasCentroSegundaaSexta44800')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados44800')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados44800')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Tres_Riachos_Viaduto_Janaina(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Tres_Riachos_Viaduto_Janaina', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta44801')
        step3 = step1.connect('SaidasBiguacuSegundaaSexta44801')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados44801')
        step5 = step1.connect('SaidasBiguacuSabadosDomingoseFeriados44801')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Tijucas(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Tijucas', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta64300')
        step3 = step1.connect('SaidasBiguacuSegundaaSexta64300')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados64300')
        step5 = step1.connect('SaidasBiguacuSabadosDomingoseFeriados64300')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Sorocaba(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Sorocaba', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta64200')
        step3 = step1.connect('SaidasCentroSegundaaSexta64200')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados64200')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados64200')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Sorocaba_Viaduto_Janaina(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Sorocaba_Viaduto_Janaina', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta64201')
        step3 = step1.connect('SaidasBiguacuSegundaaSexta64201')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados64201')
        step5 = step1.connect('SaidasBiguacuSabadosDomingoseFeriados64201')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Shopping_Center_Itaguacu(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Shopping_Center_Itaguacu', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta12400')
        step3 = step1.connect('SaidasCentroSegundaaSexta12400')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados12400')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados12400')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Saudade(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Saudade', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta44303')
        step3 = step1.connect('SaidasCentroSegundaaSexta44303')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados44303')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados44303')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Sao_Miguel(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Sao_Miguel', auto_trigger=True)
        step2 = step1.connect('SaidasEstivaSegundaaSexta10900')
        step3 = step1.connect('SaidasCentroSegundaaSexta10900')
        step4 = step1.connect('SaidasEstivaSabadosDomingoseFeriados10900')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados10900')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Santa_Maria_Antonio_Carlos(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Santa_Maria_Antonio_Carlos', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta960000')
        step3 = step1.connect('SaidasCentroSegundaaSexta960000')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados960000')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados960000')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Alto_Aririu_Florianopolis(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Alto_Aririu_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta6281')
        step3 = step1.connect('SaidasCentroSegundaaSexta6281')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados6281')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados6281')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Capela_Alto_Aririu_Florianopolis(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Capela_Alto_Aririu_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta6283')
        step3 = step1.connect('SaidasCentroSegundaaSexta6283')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados6283')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados6283')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Aririu_Caldas_Imperatriz(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Aririu_Caldas_Imperatriz', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta681')
        step3 = step1.connect('SaidasCentroSegundaaSexta681')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados681')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados681')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Aguas_Mornas_Florianopolis(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Aguas_Mornas_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta6240')
        step3 = step1.connect('SaidasCentroSegundaaSexta6240')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados6240')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados6240')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Florianopolis_Caldas_da_Imperatriz_SF_BR(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Florianopolis_Caldas_da_Imperatriz_SF_BR', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta6823')
        step3 = step1.connect('SaidasCentroSegundaaSexta6823')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados6823')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados6823')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Capela_Alto_Aririu_Florianopolis_Rod_Municipais(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Capela_Alto_Aririu_Florianopolis_Rod_Municipais', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta6282')
        step3 = step1.connect('SaidasCentroSegundaaSexta6282')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados6282')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados6282')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Florianopolis_Caldas_da_Imperatriz(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Florianopolis_Caldas_da_Imperatriz', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta680')
        step3 = step1.connect('SaidasCentroSegundaaSexta680')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados680')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados680')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Lourdes2_Florianopolis(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Lourdes2_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta970')
        step3 = step1.connect('SaidasCentroSegundaaSexta970')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados970')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados970')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Lourdes2_SA_Imperatriz(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Lourdes2_SA_Imperatriz', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta6290')
        step3 = step1.connect('SaidasCentroSegundaaSexta6290')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados6290')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados6290')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Quecaba(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Quecaba', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta660')
        step3 = step1.connect('SaidasCentroSegundaaSexta660')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados660')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados660')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def SA_Imperatriz_Florianopolis670(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_SA_Imperatriz_Florianopolis670', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta670')
        step3 = step1.connect('SaidasCentroSegundaaSexta670')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados670')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados670')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def SA_Imperatriz_Florianopolis6271(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_SA_Imperatriz_Florianopolis6271', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta6271')
        step3 = step1.connect('SaidasCentroSegundaaSexta6271')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados6271')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados6271')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def SA_Imperatriz_Florianopolis6270(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_SA_Imperatriz_Florianopolis6270', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta6270')
        step3 = step1.connect('SaidasCentroSegundaaSexta6270')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados6270')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados6270')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def SA_Imperatriz_Florianopolis6261(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_SA_Imperatriz_Florianopolis6261', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta6261')
        step3 = step1.connect('SaidasCentroSegundaaSexta6261')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados6261')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados6261')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def SA_Imperatriz_Florianopolis6260(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_SA_Imperatriz_Florianopolis6260', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta6260')
        step3 = step1.connect('SaidasCentroSegundaaSexta6260')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados6260')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados6260')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def SA_Imperatriz_Florianopolis671(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_SA_Imperatriz_Florianopolis671', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta671')
        step3 = step1.connect('SaidasCentroSegundaaSexta671')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados671')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados671')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Santa_Isabel_Florianopolis(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Santa_Isabel_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta830')
        step3 = step1.connect('SaidasCentroSegundaaSexta830')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados830')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados830')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Vargem_Grande_2_Florianopolis(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Vargem_Grande_2_Florianopolis', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta6250')
        step3 = step1.connect('SaidasCentroSegundaaSexta6250')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados6250')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados6250')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Bairro_Sao_Luiz143(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Bairro_Sao_Luiz143', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta143')
        step3 = step1.connect('SaidasCentroSegundaaSexta143')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados143')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados143')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Forquilhas08(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Forquilhas08', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta08')
        step3 = step1.connect('SaidasCentroSegundaaSexta08')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados08')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados08')
#
#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Irineu_Comelli(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Irineu_Comelli', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta676')
        step3 = step1.connect('SaidasCentroSegundaaSexta676')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados676')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados676')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Hospital_Regional(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Hospital_Regional', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta202')
        step3 = step1.connect('SaidasCentroSegundaaSexta202')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados202')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados202')

#----------------------------------------------------------------------------------------------------------------------------------------------------
    @botflow
    def Ponta_de_baixo(self, flow: FlowRoot):
        """Linha do Onibus"""
        step1 = flow.connect('horario_Ponta_de_Baixo', auto_trigger=True)
        step2 = step1.connect('SaidasBairroSegundaaSexta203')
        step3 = step1.connect('SaidasCentroSegundaaSexta203')
        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados203')
        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados203')
#
#----------------------------------------------------------------------------------------------------------------------------------------------------
#    @botflow
#    def linhadoonibus(self, flow: FlowRoot):
#        """Linha do Onibus"""
#        step1 = flow.connect('horario_linha_do_onibus', auto_trigger=True)
#        step2 = step1.connect('SaidasBairroSegundaaSexta')
#        step3 = step1.connect('SaidasCentroSegundaaSexta')
#        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados')
#        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados')
#
#----------------------------------------------------------------------------------------------------------------------------------------------------
#    @botflow
#    def linhadoonibus(self, flow: FlowRoot):
#        """Linha do Onibus"""
#        step1 = flow.connect('horario_linha_do_onibus', auto_trigger=True)
#        step2 = step1.connect('SaidasBairroSegundaaSexta')
#        step3 = step1.connect('SaidasCentroSegundaaSexta')
#        step4 = step1.connect('SaidasBairroSabadosDomingoseFeriados')
#        step5 = step1.connect('SaidasCentroSabadosDomingoseFeriados')
#
#----------------------------------------------------------------------------------------------------------------------------------------------------
