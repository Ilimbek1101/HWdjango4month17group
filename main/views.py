from django.shortcuts import render, redirect
from datetime import datetime
from .models import Director, Movie, Review
from main.forms import DirectorForm, MovieForm, RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, FormView
from django.views import View

# Create your views here.

dict_ = {
    'aboutus': 'Об истории создания и развития банка KICB: '
               '90-е годы – Проблема острой нехватки долгосрочного кредитования. Ни один местный Банк не предоставлял среднесрочное и долгосрочное финансирование.'
               '1998 год, 14 апреля – Постановлением правительства утверждается комиссия для развития проекта «Кыргызский Индустриально-Кредитный Банк»'
               '2001 год, 29 августа – Официальная церемония открытия ЗАО «Кыргызский Инвестиционно-Кредитный Банк» с уставным капиталом в 7 млн. долларов США. Банк приступил к предоставлению банковских услуг, в частности, к выдаче кредитов в размерах до 1 млн. долларов США среднему и крупному частному бизнесу.'
               '2003 год - Вследствие успешного развития Банка, Совет Директоров принял стратегическое решение о расширении спектра банковских услуг. Происходила постепенная  трансформация в универсальный банк.'
               '2006 год - Банк начал предоставлять различные розничные банковские продукты.'
               '2007 год - Один из крупнейших банков Пакистана - Хабиб Банк Лимитед - вошел в число акционеров «Кыргызского Инвестиционно-Кредитного Банка». В том же году уставный капитал Банка был увеличен до 10 млн. долларов США.'
               '2011 год - акционерный капитал Банка достиг 26,3 млн. долларов США, в июле того же года Уставный капитал был увеличен акционерами Банка до 17,5 млн. долларов США.'
               '01.03.2012 - KICB стал членом Торгово-Промышленной Палаты Кыргызской Республики.'
               '04.04.2012 - при участии KICB создается некоммерческая организация «Фонд озеленения».'
               '18.05.2012 - KICB и Министерство Социального Развития подписали соглашение о выплате социальных пособий и компенсаций на пластиковые карты Элкарт.'
               '27.12.2012 - KICB был удостоен премии Green Awards и почетной грамоты IBC (International Business Council) за достижения в области Корпоративной Социальной Ответственности'
               '21.02.2013 - KICB приобрел ЗАО «Лондон-Бишкек Иншуренс Компани» («Лондон-Бишкек страховая компания»).'
               '04.04.2013- ЗАО «Лондон-Бишкек Иншуренс Компани» («Лондон-Бишкек страховая компания») было переименовано в ЗАО «Jubilee Kyrgyzstan Insurance Company».'
               '21.08.2013 - KICB стал Принципиальным Партнером Платежной системы «UnionPay International». UnionPay International — национальная платежная система Китая. Учреждена в 2002 году как ассоциация банков КНР. Инициаторами создания выступили Государственный Совет и Народный Банк Китая.'
               '30.09.2013 - Облигации ЗАО «Кыргызский Инвестиционно-Кредитный Банк» прошли процедуру листинга на ЗАО «Кыргызская фондовая биржа» и допущены в категорию «BC» (BlueChips), что свидетельствует о высокой надежности и прозрачности KICB. Благодаря прохождению листинга, процентный доход по облигациям компании налогом не облагается.'
               '29.11.2013 - ЗАО «Кыргызский Инвестиционно-Кредитный Банк» (KICB) и Международная Финансовая Корпорация (IFC) подписали два соглашения о предоставлении кредитных ресурсов на общую сумму 12 млн. долларов США. Данные соглашения являются результатом достигнутых договоренностей между KICB и IFC в сфере кредитования по двум направлениям: малый и средний бизнес, а также поддержка торгового финансирования (экспорт и импорт) клиентов KICB.'
               '10.12.2013 - ЗАО «Кыргызский Инвестиционно-Кредитный Банк» (KICB) получил одну из самых престижных премий «Банк Года 2013» от влиятельного журнала Великобритании «The Banker» издательства The Financial Times Ltd.'
               '2013 год - KICB стал победителем в номинации «Эмитент года» по итогам ежегодного конкурса – рейтинга «Лидер Фондового Рынка» за 2013 год.'
               '11.06.2014 - KICB презентовал новую услугу - электронный кошелек «ЭЛСОМ».'
               '25.09.2014 - KICB осуществил крупнейший в истории Кыргызстана выпуск корпоративных облигаций на 150 млн. сомов.'
               '28.11.2014 - KICB признан Лучшим банком в Кыргызской Республике 2014 от влиятельного журнала Великобритании «The Banker» издательства The Financial Times Ltd.'
               '16.12.2014 - KICB признан Лучшим коммерческим банком в Кыргызской Республике 2014 года по мнению «Global Financial Market Review».'
               '25.05.2015 - KICB подписал договор о сотрудничестве с ОАО «Айыл Банк» по партнерской сети системы денежных переводов «БЕРЕКЕ».'
               '24.07.2015 - KICB получил награду «Лучший банк Кыргызстана - 2015» по версии «EUROMONEY».'
               '01.09.2015 - KICB начинает размещение третьего выпуска облигаций на сумму 200 млн. сом'
               '25.03.2016 - Кыргызский Инвестиционно-Кредитный Банк (KICB) торжественно презентовал карту UnionPay/ЭЛКАРТ.'
               '29.08.2016– KICB отметил свой 15-летний Юбилей'
               '29.08.2016– KICB официальный банк Всемирных Игр Кочевников.'
               '18.07.2017– Открытие нового филиала «Южный Манас».'
               '19.11.2018– KICB признан лучшим в номинациях «Лучший коммерческий банк Кыргызстана 2018» и «Лучший инновационный продукт в розничном кредитовании 2018» по версии международного финансово – аналитического издания «International Banker».'
               '19.12.2018– KICB признан лучшим банком 2018 года в Кыргызской Республике по версии журнала «The Banker» издательства The Financial Times Ltd.'
               '12.02.2019– KICB начал обслуживание карт Mastercard'
               '24.10.2019– KICB с ГИК подписали официальное Соглашение о реализации «Программы жилищного финансирования».'
               '04.12.2019– KICB стал обладателем одной из самых престижных премий «Лучший Банк Года 2019» по версии журнала «The Banker» издательства Financial Times.'
               '24.08.2020– KICB представил премиальную карту –Visa Infinite.'
               '04.12.2020– KICB открыл Центр Розничного Обслуживания - и  VIP центр Банка.'
               '09.02.2021– Открытие нового филиала «Орто-Сай».'
               '09.03.2021– KICB приобрел 100% акций ЗАО «Первая МикроФинансовая Компания».'
               '29.08.2021– KICB отметил свой 20-летний Юбилей',
    'sitestruc': 'Для ознакомления воспользуйтесь картой сайта: '
                 'Карта сайта Главная страница О банке Алдыга койгон максаттар / Видение и ценности Тарых / История Акционерлер / Акционеры Наши новости Ачылыш аземи / Церемония Открытия КСЖ / КСО KICBде иштөө / Работа в KICB Бишкек шаары жана Чүй областы / г. Бишкек и Чуйская область Депозиттер боюнча адис-кассир / Специалист по депозитам-кассир Бизнести өнүктүрүү башчысы/Начальник Отдела по развитию бизнеса Адис / Специалист Тармактык Коопсуздук Адиси / Специалист Сетевой Безопасности Тармак администратору / Сетевой администратор Стажёр (Насыя боюнча кенже адис) / Стажёр (Младший кредитный специалист) Микронасыялоо боюнча адис/ Специалист по микрокредитованию Микронасыялоо боюнча улук адис / Старший специалист по микрокредитованию Чакан жана орто бизнестин адиси / Специалист малого и среднего бизнеса Аманаттар боюнча адис / Специалист по депозитам Кыргыз тилин өнүктүрүү боюнча координатор / Координатор по развитию кы IT аудит бөлүмүнүн башчысы/Начальник Отдела ИТ аудита Разработчик ПО Специалист малого и среднего бизнеса Ош областы / Ошская область Кредиттик адис / Кредитный специалист Микронасыялоо боюнча адис/ Специалист по микрокредитованию Микронасыялоо боюнча улук адис / Старший специалист по микрокредитованию Чакан жана орто бизнестин адиси / Специалист малого и среднего бизнеса Жалал-Абадская область Кредиттик адис / Кредитный специалист Нарынская область Чакан жана орто бизнес боюнча адис / Специалист малого и среднего бизнеса Иссык-Кульская область Баткенская область Таласская область Финансылык отчет / Финансовая отчетность Басма сөз банк жөнүндө / Пресса о нас Сыйлыктар / Награды 2013 2014 2015 2018 2019 Жетекчилик / Руководство Корпоративным клиентам Эсептешүү-кассалык тейлөө / Расчетно-кассовое обслуживание Күндөлүк эсептешүү эсеби / Текущий расчетный счет Конверсиондук операциялар / Конверсионные операции Юридикалык жактар үчүн сейфтик ячейкалар / Сейфовые ячейки для юридических лиц Төлөм тапшырмасын толтуруу эрежелери / Правила заполнения платежного поручения Депозиттер / Депозиты Облигациялар / Облигации Банктык карттар / Банковские карты Эмгек акы долбоорлору / Зарплатные проекты VISA Business карты / Банковская карта VISA Business Mastercard Business Банкоматтар жана ПОС-терминалдар / Банкоматы и ПОС-терминалы «Достук ымалашуу» түйүнү / Дружественная сеть Карт ээлери үчүн маалымат / Информация владельцу банковской карты Карт ээлерине банкомат менен иш алып баруу жагында маалымат берүү / Информация владельцу Дайыма берилүүчү суроолор / Часто задаваемые вопросы Пайдалуу кеңештер / Полезные советы Соода эквайринги / Торговый эквайринг Интернет Эквайринг Корпоративдик кредиттер / Корпоративные кредиты Инвестициялык максаттар үчүн корпоративдик насыя / Корп. кредит на инвестиционные цели Жүгүртүү капиталына корпоративдик насыя / Корп. кредит на оборотные средства "Энергия үнөмдөөчү" кредит / Кредит "Энергосберегающий" Энергия үнөмдөөчү продукцияларды жасап чыгаруучулар/сунуштоочулар  Энергияны көпкө сактаган продукция сатып алуучулар үчүн “Энергия үн Корпоративдик насыялык линиясы / Корпоративная кредитная линия ЭЛСОМ электрондук капчыгы / Электронный кошелек ЭЛСОМ Соода ишин каржылоо / Торговое финансирование Экспорттук аккредитив / Экспортный аккредитив Схема работы аккредитива Импорттук аккредитив / Импортный аккредитив Документ түрүндөгү инкассонун схемасы / Схема работы документарного инкассо Банк гарантиялары / Банковские гарантии Юридикалык жактар үчүн тарифтер / Тарифы для юридических лиц Камсыздандыруу кызмат көрсөтүүлөрү / Страховые услуги МБК / ГЦБ Мамлекеттик баалуу кагаздарга инвестициялоо / Инвестиции в Государственные ценные бумаги Брокердик ишмердик / Брокерская деятельность Частным клиентам Банк эсеби / Банковский счет Аманаттар / Вклады «Мөөнөттүү» аманат / Вклад «Срочный» «Топтолмо» аманаты / Вклад «Накопительный» «Балдар үчүн» аманаты / Вклад «Детский» Облигациялар / Облигации Облигациялардын биринчи чыгарылышы / Первый выпуск облигаций Облигациялардын экинчи чыгарылышы / Второй выпуск облигаций Облигациялардын үчүнчү чыгарылышы / Третий выпуск облигаций Облигациялардын төртүнчү чыгарылышы / Четвертый выпуск облигаций Облигацияларынын бешинчи чыгарылышы / Пятый выпуск облигаций KICB облигацияларынын алтынчы чыгарылышы / Шестой выпуск облигаций KICB Банктык карттар / Банковские карты Виды карт Visa Electron Visa Classic Visa Gold Элкарт/UnionPay карты / Карта Элкарт/UnionPay Mastercard Standard Mastercard Gold Visa Infinite Дароо чыгарылган карттар / Предвыпущенные карты «Персоналдык» Элкарт / Банковская карта Элкарт «Персональная» Пенсионер карты / Карта Пенсионера Социалдык төлөөлөр / Социальные Выплаты Кошумча мүмкүнчүлүк / Дополнительные возможности Кардардын дизайны боюнча чыгарылган карттар! / Карта с Вашим дизайном! Өзгөчө дизайндагы картка буйрутма / Заказ карты с индивидуальным дизайном Акча которуулар / Денежные переводы SMS-билдирүү / SMS-оповещение Карт боюнча овердрафт / Овердрафт Беш эмгек акы / Кредит «Пять зарплат» Дисконттук программа / Дисконтная Программа Партнерам QIWI которуулары / Переводы QIWI Услуга 3D Secure Банкоматтар / Банкоматы Карттарды толуктоо / Пополнение карт Важная информация Пайдалуу кеңештер / Полезные советы Дайыма берилүүчү суроолор / Часто задаваемые вопросы Кредиттер / Кредиты Бизнес кредиттер / Бизнес кредиты Бизнес кредит Агрокредит Необходимые документы Россия-Кыргыз өнүктүрүү фондусунун бизнести максаттуу каржылоо програм Энергияны үнөмдөө / Энергоэффективный Микрокредиты Керектөө кредиттери / Потребительские кредиты Жашоо ырахаты / Радости жизни Беш эмгек акы / Пять зарплат Овердрафт Бизнес-Овердрафт «Жылуу үй» жана «Жылуу үй +» / Теплый дом и Теплый дом + «Товар үчүн бөлүп төлөө» кредити / ЭЛСОМ кредиттери / Кредиты ЭЛСОМ Агенттер үчүн «ЭЛСОМ» кредити / Кредит «ЭЛСОМ» для агентов Ипотекалык кредиттер / Ипотечное кредитование Ипотекалык кредит / Ипотечное кредитование Аманат ипотекасы / Сберегательная ипотека Турак жайды каржылоо программасы / Программа Жилищного Финансирования Талап кылынган документтер / Необходимые документы Акча которуулар / Денежные переводы ЭЛСОМ электрондук капчыгы / Электронный кошелек ЭЛСОМ Сейфтик ячейкалар (чөнөктөр) / Сейфовые ячейки Төлөм терминалы / Платежные терминалы KICB төлөм терминалдарынын тизмеси / Список платежных терминалов KICB Дайыма берилип туруучу суроолор / Часто встречающиеся вопросы Салыктар боюнча маалымкат / Справка по налогам Жеке адамдар жана жеке ишкерлер үчүн тарифтер / Тарифы для физических лиц Страховые услуги МБК / ГЦБ Мамлекеттик баалуу кагаздарга инвестициялоо / Инвестиции в Государственные ценные бумаги Брокердик ишмердик / Брокерская деятельность Жеке акча алмаштыруу курстары / Индивидуальные обменные курсы АКЦИЯЛАР / АКЦИИ Акция «Бесплатный Страховой Ваучер» KICB снижает процентные ставки по бизнес-кредитам! KICB снижает процентные ставки по бизнес-кредитам! KICBнин төлөм реквизиттери / Платежные реквизиты KICB Эсептерди сунуштоо үчүн реквизиттер / Реквизиты для выставления счетов Корреспонденттик түйүн / Корреспондентская сеть Поиск Сатып өткөрүлүүчү мүлктөр / Реализуемое имущество Интернет-банкинг i-bank Банк-кардар / Банк-клиент Картты толуктоо ыкмалары / Способы пополнения карт Visa KICB банктык картанын карт-эсебине акча каражаттарды которуу үчүн төлөм Страховые услуги Жеке адамдар үчүн / Физическим лицам КАСКО камсыздандыруусу / Страхование КАСКО ДСАГО камсыздандыруу / Страхование ДСАГО Лизингди камсыздандыруу/Страхование лизинга Камсыздандыруунун критерийлери / Критерии страхования «Акысыз Камсыздандыруу Ваучери» Акциясы / Акция «Бесплатный Страховой Ваучер» Почему страховая компания «Jubilee Kyrgyzstan»? Камсыздандыруу полистерин сатып ала турган КИКБ филиалдарынын даректери / Банктын китепчелери / Брошюры банка Контакты Иш орундар / Вакансии Даттанууларды жана сунуштарды кароо тартиби / Порядок рассмотрения жалоб и предложений Окуу борбору / Тренинг центр',
    'time': f'{datetime.now()}'
}


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', context=dict_)


class StrucView(View):
    def get(self, request):
        return render(request, 'struc.html', context=dict_)


class TimeView(View):
    def get(self, request):
        return render(request, 'now.html', context=dict_)



class ContextData(object):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['director_list'] = Director.objects.all()
        return context


class DirectorListView(ContextData, ListView):
    queryset = Director.objects.all()
    template_name = 'directors.html'
    # context_object_name = 'director_list'


#     return context
#     # queryset = Director.objects.all()
#     # template_name = 'directors.html'
#     # context_object_name = 'movie_list'

# def director_list_view(request):
#     print(request.user)
#     directors = Director.objects.all()
#     context = {
#         'director_list': directors
#     }
#     print(directors)
#     return render(request, 'directors.html', context=context)

# def movie_list_view(request):
#     movies = Movie.objects.all()
#     print(movies)
#     return render(request, 'movies.html', context={
#         'movie_list': movies,
#         'director_list': Director.objects.all()
#     })


class MovieListView(ContextData, ListView):
    queryset = Movie.objects.all()
    template_name = 'movies.html'
    context_object_name = 'movie_list'


class ReviewListView(ContextData, ListView):
    queryset = Review.objects.all()
    template_name = 'reviews.html'
    context_object_name = 'review_list'



# def review_list_view(request):
#     print(Review.objects.all())
#     return render(request, 'reviews.html', context={
#         'review_list': Review.objects.all(),
#         'movie_list': Movie.objects.all()
#     })



class DirectorDetailView(ContextData, DetailView):
    model = Director
    template_name = 'directordetail.html'
    context_object_name = 'director_detail'

# def director_detail_view(request, id):
#     director = Director.objects.get(id=id)
#     return render(request, 'directordetail.html', context={'director_detail': director})


# def movie_detail_view(request, id):
#     movie = Movie.objects.get(id=id)
#     review = Review.objects.get(id=id)
#     return render(request, 'moviedetail.html', context={'movie_detail': movie,
#                                                         'director_list': Director.objects.all(),
#                                                         'review_list': Review.objects.filter(movie_id=id)})


class MovieDetailView(ContextData, DetailView):
    model = Movie
    template_name = 'moviedetail.html'
    context_object_name = 'movie_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['review_list'] = Review.objects.filter(movie=self.object)
        return context


class ReviewDetailView(ContextData, DetailView):
    model = Review
    template_name = 'reviewdetail.html'
    context_object_name = 'review_detail'



# def review_detail_view(request, id):
#     print(request.user)
#     review = Review.objects.get(id=id)
#     return render(request, 'reviewdetail.html', context={'review_detail': review})


def director_movie_filter_view(request, director_id):
    context = {
        'movie_list': Movie.objects.filter(director_id=director_id),
        'director_list': Director.objects.all()
    }
    return render(request, 'movies.html', context=context)


class DirectorMovieFilterView(ContextData, ListView):
    queryset = Movie.objects.all()
    template_name = 'movies.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return Movie.objects.filter(director_id=self.request.resolver_match.kwargs['director_id'])


class MovieReviewFilterView(ContextData, ListView):
    queryset = Review.objects.all()
    template_name = 'reviews.html'
    context_object_name = 'review_list'

    def get_queryset(self):
        return Review.objects.filter(movie=self.request.resolver_match.kwargs['movie_id'])

# def movie_review_filter_view(request, movie_id):
#     context = {
#         'review_list': Review.objects.filter(movie_id=movie_id),
#         'movie_list': Movie.objects.all()
#     }
#     return render(request, 'reviews.html', context=context)

class AddDirectorFormView(ContextData, FormView):
    form_class = DirectorForm
    template_name = 'add_director.html'
    success_url = '/directors/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# def add_director_view(request):
#     form = DirectorForm()
#     if request.method == 'POST':
#         form = DirectorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/directors/')
#     return render(request, 'add_director.html', context={
#         'form': form,
#         'director_list': Director.objects.all()
#     })

class AddMovieFormView(ContextData, FormView):
    form_class = MovieForm
    template_name = 'add_movie.html'
    success_url = '/movies/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# def add_movie_view(request):
#     form = MovieForm()
#     if request.method == 'POST':
#         form = MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/movies/')
#     return render(request, 'add_movie.html', context={
#         'form': form,
#         'director_list': Director.objects.all()
#     })


class RegisterFormView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# def register_view(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/register/', )
#     return render(request, 'register.html', context={
#         'form': form
#     })

class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/login/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        # email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user=user)
        return super().form_valid(form)

# def login_view(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             # email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user=user)
#             return redirect('/login/')
#     return render(request, 'login.html', context={
#         'form': form
#     })

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')