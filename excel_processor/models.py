from django.db import models

# Create your models here.

class Kit_data (models.Model):

    MINI_TRILHO = "MINI TRILHO"
    COLONIAL = "COLONIAL"
    FIBROMADEIRA = "FIBROMADEIRA"
    FIBROMETALICO = "FIBROMETALICO"
    ROMANA_AMERICANA = "ROMANA/AMERICANA"
    ZINCO_ALIZINCO = "ZINCO/ALUZINCO"
    SEM_ESTRUTURA = "SEM ESTRUTURA"

    escolha_de_tipos_de_telhados = [
        (MINI_TRILHO, "MINI TRILHO"),
        (COLONIAL, "COLONIAL"),
        (FIBROMADEIRA, "FIBROMADEIRA"),
        (FIBROMETALICO, "FIBROMETALICO"),
        (ROMANA_AMERICANA, "ROMANA/AMERICANA"),
        (ZINCO_ALIZINCO, "ZINCO/ALUZINCO"),
        (SEM_ESTRUTURA, "SEM ESTRUTURA")

    ]

    identificacao_kit = models.CharField(("Identificacao do kit"),
                                         max_length=8000)
    codigo = models.IntegerField(("Codigo de identificacao"),  
                                   unique=True)
    preco = models.FloatField(("Preço"))
    telhado = models.CharField(("Tipo de Telhado"),
                                choices=escolha_de_tipos_de_telhados,
                                max_length=8000)
    conexao =  models.CharField(("Conexão"), 
                                max_length=8000)
    qnt_modulos = models.IntegerField(("Quantidade de Modulos"))
    mod_modulo = models.CharField(("Modelo do Modulo"), 
                                    max_length=8000)
    potencia_unitaria = models.IntegerField(("Potencia Unitaria Modulo"))
    max_overload = models.IntegerField(("Overload Maximo"))
    kwp = models.FloatField(("kWp"))
    qnt_inversor1 = models.IntegerField(("Quantidade de inversor 1"), null=True, blank=True)
    invesor1 = models.CharField(("inversor 1"), 
                                    null=True, 
                                    blank=True, 
                                    max_length=8000)
    qnt_inversor2 = models.IntegerField(("Quantidade de inversor 2"), 
                                            null=True, 
                                            blank=True)
    invesor2 = models.CharField(("inversor 2"), 
                                    null=True, 
                                    blank=True, 
                                    max_length=8000)
    qnt_cabo_vermelho_m = models.CharField(("Quantidade de Cabo Vermelho Metros"), 
                                            max_length=8000)
    mod_cabo_vermelho = models.CharField(("Modelo Do Cabo Vermelho"), 
                                            null=True, 
                                            blank=True,
                                            max_length=8000)
    qnt_cabo_preto_m = models.CharField(('Quantidade de Cabo preto (Metros)'), 
                                            max_length=8000)
    mod_cabo_preto = models.CharField(("Modelo Do Cabo Preto"), 
                                        null=True, 
                                        blank=True, 
                                        max_length=8000)
    qnt_pares_conectores = models.IntegerField(("Quantidade de Conectores Pares"))
    mod_par_conector = models.CharField(("Modelo de Conector par"), 
                                            max_length=8000)
    qnt_stringbox = models.IntegerField(("Quantidade Stringbox"))
    mod_stringbox = models.CharField(("Modelos Stringbox"), 
                                        max_length=8000)
    qnt_estrutura1 = models.IntegerField(("Quantidade de estruturas 1"))
    mod_estrutura1 = models.CharField(("Modelo Estrutura 1"), 
                                        max_length=8000)
    qnt_estrutura2 = models.IntegerField(("Quantidade de estruturas 2"), 
                                            null=True, 
                                            blank=True)
    mod_estrutura2 = models.CharField(("Modelo Estrutura 2"), 
                                        null=True, 
                                        blank=True, 
                                        max_length=8000)
    qnt_estrutura3 = models.IntegerField(("Quantidade de estruturas 3"), 
                                            null=True, 
                                            blank=True)
    mod_estrutura3 = models.CharField(("Modelo Estrutura 3"), 
                                        null=True, 
                                        blank=True, 
                                        max_length=8000)
    qnt_estrutura4 = models.IntegerField(("Quantidade de estruturas 4"), 
                                         null=True, 
                                         blank=True)
    mod_estrutura4 = models.CharField(("Modelo Estrutura 4"), 
                                      null=True, 
                                      blank=True, 
                                      max_length=8000)
    qnt_estrutura5 = models.IntegerField(("Quantidade de estruturas 5"), 
                                         null=True, 
                                         blank=True)
    mod_estrutura5 = models.CharField(("Modelo Estrutura 5"), 
                                      null=True, 
                                      blank=True, 
                                      max_length=8000)
    marca_inversor = models.CharField(("Marca do inversor"), 
                                      max_length=8000)
    mod_modulo = models.CharField(("Marca do Modulo"), 
                                  max_length=8000) 

    class Meta:
        verbose_name = ("Kit_data")
        verbose_name_plural = ("Kits_data")

    def __str__(self):
        return self.identificacao_kit