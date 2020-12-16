from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)



class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

    risk_choices = [0,1,2,3,4,5,6,7,8,9,10]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    risk = models.IntegerField(
        label='Genel olarak ne kadar risk alırsınız? 0 = kesinlikle risk almam, 10 = kesinlikle risk alırım.',
        choices=Constants.risk_choices,
        widget=widgets.RadioSelectHorizontal  
    )
    loss1 = models.StringField(
        label= ' Aşağıdaki alternatiflerden hangisini tercih edersiniz?',
        choices=['Kesin olarak 475 TL kazanacaksınız', '%25 ihtimalle 2000TL kazanacaksınız, %75 ihtimalle kazancınız olmayacak'],
        widget=widgets.RadioSelect  
    )
    loss2 = models.StringField(
        label='Aşağıdaki alternatiflerden hangisini tercih edersiniz?',
        choices=['Kesin olarak 725 TL kaybedeceksiniz', '%75 ihtimalle 1000TL kaybedeceksiniz, %25 ihtimalle kaybınız olmayacak'],
        widget=widgets.RadioSelect  
    )
        
    age = models.IntegerField(
        label='Yaşınız',
        min=13, max=80)

    gender = models.StringField(
        choices=['Erkek', 'Kadın'],
        label='Cinsiyetiniz',
        widget=widgets.RadioSelect)

    year = models.IntegerField(
        label='BİLGİ ye giriş yılınız',
        min=2000, max=2020)
    
    dept = models.StringField(
        label='Bölümünüz')
    
    scholarship = models.StringField(
        choices=['Tam Burslu', '%75 Burslu', '%50 Burslu', '%25 Burslu', 'Burssuz'],
        label='ÖSYM başarı Burs durumunuz',
        widget=widgets.RadioSelect)
    
    father = models.StringField(
        choices=['Hiç okula gitmemiş', 'İlk veya orta öğretim', 'Lise', 'Ön lisans / Meslek Yüksek okulu',
         'Üniversite (Lisans)', 'Yüksek Lisans', 'Doktora'],
        label='Babanızın son mezun olduğu eğitim kurumunu hangisi en iyi ifade eder?',
        widget=widgets.RadioSelect)

    mother = models.StringField(
        choices=['Hiç okula gitmemiş', 'İlk veya orta öğretim', 'Lise', 'Ön lisans / Meslek Yüksek okulu',
         'Üniversite (Lisans)', 'Yüksek Lisans', 'Doktora'],
        label='Annenizin son mezun olduğu eğitim kurumunu hangisi en iyi ifade eder?',
        widget=widgets.RadioSelect)
    experiment = models.StringField(
        choices=['Evet', 'Hayır'],
        label='Daha önce bir BELİS deneyine katıldınız mı?',
        widget=widgets.RadioSelect)

    tercih = models.StringField(
        label='Deneydeki kararlarınızı nasıl aldığınızı açıklayınız.')

    tercih_2 = models.StringField(
        label=" Deneydeki kararlarınızı en iyi açıklayan seçeneği seçiniz. ",
        widget=widgets.RadioSelect(
        choices=(
                (0, "İlk iki turda bilgisayar Yeşil seçmişse 3. Turda Yeşil seçme olasılığının %50 olduğunu düşündüm."),
                (1, "İlk iki turda bilgisayar Yeşil seçmişse 3. Turda Yeşil seçme olasılığının %40-%50 arasında olduğunu düşündüm."),
                (2, "İlk iki turda bilgisayar Yeşil seçmişse 3. Turda Yeşil seçme olasılığının %30-%40 arasında olduğunu düşündüm."),
                (3, "İlk iki turda bilgisayar Yeşil seçmişse 3. Turda Yeşil seçme olasılığının %20-%30 arasında olduğunu düşündüm."),
                (4, "İlk iki turda bilgisayar Yeşil seçmişse 3. Turda Yeşil seçme olasılığının %20den daha az olduğunu düşündüm."),
                
            )
        ),
    )
    tercih_3 = models.StringField(
        label=" Deneydeki kararlarınızı en iyi açıklayan seçeneği seçiniz.  ",
        widget=widgets.RadioSelect(
        choices=(
                (0, "Herhangi bir turda bilgisayar Yeşil seçmişse bir sonraki turda Yeşil seçme olasılığının %50 olduğunu düşündüm."),
                (1, "Herhangi bir turda bilgisayar Yeşil seçmişse bir sonraki turda Yeşil seçme olasılığının %40-%50 arasında olduğunu düşündüm."),
                (2, "Herhangi bir turda bilgisayar Yeşil seçmişse bir sonraki turda Yeşil seçme olasılığının %30-%40 arasında olduğunu düşündüm."),
                (3, "Herhangi bir turda bilgisayar Yeşil seçmişse bir sonraki turda Yeşil seçme olasılığının %20-%30 arasında olduğunu düşündüm."),
                (4, "Herhangi bir turda bilgisayar Yeşil seçmişse bir sonraki turda Yeşil seçme olasılığının %20den daha az olduğunu düşündüm."),
            )
        ),
    )

    
