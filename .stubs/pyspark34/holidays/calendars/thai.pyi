from _typeshed import Incomplete
from datetime import date

KHMER_CALENDAR: str
THAI_CALENDAR: str

class _ThaiLunisolar:
    '''
    ** Thai Lunar Calendar Holidays only work from 1941 (B.E. 2484) onwards
       until 2057 (B.E. 2600) as we only have Thai year-type data for
       cross-checking until then.

    So here are the basics of the Thai Lunar Calendar
        3-year types for calendar intercalation:
            - Pakatimat (Normal Year):
                    consist of 12 months, has 354 days.
            - Athikawan (Extra-Day Year):
                    add a day to the 7th month of the year, has 355 days
                    for the synodic month correction.
            - Athikamat (Extra-Month Year):
                    we have the 8th month twice, has 384 days for the
                    sidereal year correction.

        Each month either has 30 (Even months) or 29 (Odd months)
            - The waxing phase has 15 days until Full Moon and waning
                phase 14 (Odd Months)/15 (Even Months/
                Month 7 of Athikawan years) days for the New Moon.
            - The second "Month 8" for Athikamat years is called
                "Month 8.8", with all observed holy days delayed from
                the usual calendar by 1 month.

    List of public holidays dependent on the Thai Lunar Calendar:
        - Magha Puja/Makha Bucha/Meak Bochea:
                15th Waxing Day (Full Moon) of Month 3
                (On Month 4 for Athikamat Years).
                KHMER_CALENDAR always fall on Month 3.
        - Vesak/Visakha Bucha/Visaka Bochea:
                15th Waxing Day (Full Moon) of Month 6
                (On Month 7 for Athikamat Years).
                KHMER_CALENDAR always fall on Month 6.
        - Thai Royal Ploughing Ceremony/Raeknakhwan:
                Based on this, though Court Astrologer picks the
                auspicious dates, which sadly don\'t fall into a
                predictable pattern; see its specific section below.
        - Cambodian Royal Ploughing Ceremony/Preah Neangkol:
                4th Waning Day of Month 6
                (On Month 7 for Athikamat Years).
                This defaults to KHMER_CALENDAR (its sole user).
        - Asalha Puja/Asarnha Bucha:
                15th Waxing Day (Full Moon) of Month 8
                (On Month 8/8 for Athikamat Years).
                KHMER_CALENDAR always fall on Month 8.
        - Buddhist Lent Day/Wan Khao Phansa:
                1st Waning Day of Month 8
                (On Month 8/8 for Athikamat Years).
                KHMER_CALENDAR always fall on Month 8.
        - Pchum Ben/Prachum Bandar:
                15th Waning Day (New Moon) of Month 10.
        - Loy Krathong/Boun That Louang/Bon Om Touk:
                15th Waxing Day (Full Moon) of Month 12.

    Other Buddhist date on Thai Lunar Calendar:
        - Buddha\'s Cremation Day/Atthami Bucha
                8th Waning Day of  Month 6
                (On Month 7 for Athikamat Years).
                KHMER_CALENDAR always fall on Month 6
        - End of Buddhist Lent Day/Ok Phansa:
                15th Waxing Day (Full Moon) of Month 11

    The following code is based on Ninenik Narkdee\'s PHP implementation,
    and we\'re thankful for his work.

    Please avoid touching the Athikawan and Athikamat declaration array
    at all costs unless you can find sources for them somewhere for 2057++

    Sources: (Ninenik.com \'s wbm) http://tiny.cc/wa_ninenik_thluncal_php
             https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2560.aspx

    Usage example:

    >>> from holidays.utils import _ThaiLunisolar
    >>> thls = _ThaiLunisolar()
    >>> print(thls.visakha_bucha_date(2010))
    2010-05-28
    '''
    ATHIKAWAN_YEARS_GREGORIAN: Incomplete
    ATHIKAMAT_YEARS_GREGORIAN: Incomplete
    START_DATE: Incomplete
    START_YEAR: int
    END_YEAR: int
    def __init__(self, calendar=...) -> None: ...
    def makha_bucha_date(self, year: int, calendar: Incomplete | None = None) -> date | None:
        '''
        Calculate the estimated Gregorian date of Makha Bucha.
        If the Gregorian year input is invalid, this will outputs None instead.

        Also known as "Magha Puja", "Makha Buxha" and "Meak Bochea".
        This coincides with the 15th Waxing Day of Month 3
        in Thai Lunar Calendar, or Month 4 in Athikamat years.

        KHMER_CALENDAR will always use Month 3 regardless of year type.

        To calculate, we use use the following time delta:
        - Athikamat: 15th Waxing Day of Month 4
                     or 29[1] + 30[2] + 29[3] + 15[4] -1 = 102
        - Athikawan: 15th Waxing Day of Month 3
                     or 29[1] + 30[2] + 15[3] -1 = 73
        - Pakatimat: 15th Waxing Day of Month 3
                     or 29[1] + 30[2] + 15[3] -1 = 73

        :param year:
            The Gregorian year.

        :param calendar:
            Calendar type, this defaults to THAI_CALENDAR.

        :return:
            Estimated Gregorian date of Makha Bucha.
        '''
    def visakha_bucha_date(self, year: int, calendar: Incomplete | None = None) -> date | None:
        '''
        Calculate the estimated Gregorian date of Visakha Bucha.
        If the Gregorian year input is invalid, this will outputs None instead.

        Also known as "Vesak" and "Buddha Day". This coincides with
        the 15th Waxing Day of Month 6 in Thai Lunar Calendar, or Month 7 in Athikamat years.

        KHMER_CALENDAR will always use Month 6 regardless of year type.

        To calculate, we use use the following time delta:
        - Athikamat: 15th Waxing Day of Month 7
                     or 177[1-6] + 15[7] -1 = 191
        - Athikawan: 15th Waxing Day of Month 6
                     or 147[1-5] + 15[6] -1 = 161
        - Pakatimat: 15th Waxing Day of Month 6
                     or 147[1-5] + 15[6] -1 = 161

        :param year:
            The Gregorian year.

        :param calendar:
            Calendar type, this defaults to THAI_CALENDAR.

        :return:
            Estimated Gregorian date of Visakha Bucha.
        '''
    def preah_neangkoal_date(self, year: int) -> date | None:
        '''
        Calculate the estimated Gregorian date of Preah Neangkoal.
        If the Gregorian year input is invalid, this will outputs None instead.

        Also known as "Cambodian Royal Ploughing Ceremony". This always
        coincides with the 4th Waning Day of Month 6 in Khmer Lunar Calendar.

        To calculate, we use use the following time delta:
        - Athikamat: 15th Waxing Day of Month 6
                     or 177[1-6] + 19[7] -1 = 165
        - Athikawan: 15th Waxing Day of Month 6
                     or 147[1-5] + 19[6] -1 = 165
        - Pakatimat: 15th Waxing Day of Month 6
                     or 147[1-5] + 19[6] -1 = 165
        Or as in simpler terms: "Visakha Bucha" +4

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Preah Neangkoal.
        '''
    def atthami_bucha_date(self, year: int, calendar: Incomplete | None = None) -> date | None:
        '''
        Calculate the estimated Gregorian date of Atthami Bucha.
        If the Gregorian year input is invalid, this will outputs None instead.

        Also known as "Buddha\'s Cremation Day". This coincides with
        the 8th Waning Day of Month 6 in Thai Lunar Calendar, or Month 7 in Athikamat years.

        KHMER_CALENDAR will always use Month 6 regardless of year type.

        To calculate, we use use the following time delta:
        - Athikamat: 8th Waning Day of  Month 7
                    or 177[1-6] + 23[7] -1 = 199
        - Athikawan: 8th Waning Day of  Month 6
                     or 147[1-5] + 23[6] -1 = 169
        - Pakatimat: 8th Waning Day of  Month 6
                    or 147[1-5] + 23[6] -1 = 169
        - Or as in simpler terms: "Visakha Bucha" +8

        :param year:
            The Gregorian year.

        :param calendar:
            Calendar type, this defaults to THAI_CALENDAR.

        :return:
            Estimated Gregorian date of Atthami Bucha.
        '''
    def asarnha_bucha_date(self, year: int) -> date | None:
        '''
        Calculate the estimated Gregorian date of Asarnha Bucha.
        If the Gregorian year input is invalid, this will outputs None instead.

        Also known as "Asalha Puja". This coincides with
        the 15th Waxing Day of Month 8 in Thai Lunar Calendar,
        or Month 8.8 in Athikamat years.

        Lao Start of Buddhist Lent start on this day (1-day earlier than Thai and Khmer ones).

        To calculate, we use use the following time delta:
        - Athikamat: 15th Waxing Day of Month 8/8
                     or 177[1-6] + 29[7] + 30[8] + 15[8.8] -1 = 250
        - Athikawan: 15th Waxing Day of Month 8
                     or 177[1-6] + 30[7] + 15[8] -1 = 221
        - Pakatimat: 15th Waxing Day of Month 8
                     or 177[1-6] + 29[7] + 15[8] -1 = 220

        :param year:
            The Gregorian year.

        :param calendar:
            Calendar type, this defaults to THAI_CALENDAR.

        :return:
            Estimated Gregorian date of Asarnha Bucha.
        '''
    def khao_phansa_date(self, year: int) -> date | None:
        '''
        Calculate the estimated Gregorian date of Khao Phansa.
        If the Gregorian year input is invalid, this will outputs None instead.

        Also known as "(Start of) Buddhist Lent" and "Start of Vassa".
        This coincides with the 1st Waning Day of Month 8
        in Thai Lunar Calendar, or Month 8.8 in Athikamat years.

        To calculate, we use use the following time delta:
        - Athikamat: 1st Waning Day of Month 8.8
                     or 177[1-6] + 29[7] + 30[8] + 16[8.8] -1 = 251
        - Athikawan: 1st Waning Day of Month 8 ]
                     or 177[1-6] + 30[7] + 16[8] -1 = 222
        - Pakatimat: 1st Waning Day of Month 8
                     or 177[1-6] + 29[7] + 16[8] -1 = 221
        - Or as in simpler terms: "Asarnha Bucha" +1

        :param year:
            The Gregorian year.

        :param calendar:
            Calendar type, this defaults to THAI_CALENDAR.

        :return:
            Estimated Gregorian date of Khao Phansa.
        '''
    def boun_haw_khao_padapdin_date(self, year: int) -> date | None:
        '''
        Calculate the estimated Gregorian date of Boun Haw Khao Padapdin.
        If the Gregorian year input is invalid, this will outputs None instead.

        Also known as "Boon Khao Padap Din".
        This coincides with the 14th Waning Day of Month 9 in Thai Lunar Calendar.

         To calculate, we use use the following time delta:
        - Athikamat: 14th Waning Day of Month 9
                     or 236[1-8] + 30[8.8] + 29[9] -1 = 294
        - Athikawan: 14th Waning Day of Month 9
                     or 236[1-8] + 1[7] + 29[9] -1 = 265
        - Pakatimat: 14th Waning Day of Month 9
                     or 236[1-8] + 29[9] -1 = 264

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Boun Haw Khao Padapdin.
        '''
    def boun_haw_khao_salark_date(self, year: int) -> date | None:
        '''
        Calculate the estimated Gregorian date of Boun Haw Khao Salark.
        If the Gregorian year input is invalid, this will outputs None instead.

        Also known as "Boon Khao Sak".
        This coincides with the 15th Waxing Day of Month 10 in Thai Lunar Calendar.

         To calculate, we use use the following time delta:
        - Athikamat: 15th Waxing Day of Month 10
                     or 265[1-9] + 30[8.8] + 15[10] -1 = 309
        - Athikawan: 15th Waxing Day of Month 10
                     or 265[1-9] + 1[7] + 15[10] -1 = 280
        - Pakatimat: 15th Waxing Day of Month 10
                     or 265[1-9] + 15[10] -1 = 279

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Pchum Ben.
        '''
    def pchum_ben_date(self, year: int) -> date | None:
        '''
        Calculate the estimated Gregorian date of Pchum Ben.
        If the Gregorian year input is invalid, this will outputs None instead.

        Also known as "Prachum Bandar".
        This coincides with the 15th Waning Day of Month 10 in Thai Lunar Calendar.

         To calculate, we use use the following time delta:
        - Athikamat: 15th Waning Day of Month 10
                     or 265[1-9] + 30[8.8] + 30[10] -1 = 324
        - Athikawan: 15th Waning Day of Month 10
                     or 265[1-9] + 1[7] + 30[10] -1 = 295
        - Pakatimat: 15th Waning Day of Month 10
                     or 265[1-9] + 30[10] -1 = 294

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Pchum Ben.
        '''
    def ok_phansa_date(self, year: int) -> date | None:
        '''
        Calculate the estimated Gregorian date of Ok Phansa.
        If the Gregorian year input is invalid, this will outputs None instead.

        Also known as "End of Buddhist Lent" and "End of Vassa".
        This coincides with the 15th Waxing Day of Month 11 in Thai Lunar Calendar.

        To calculate, we use use the following time delta:
        - Athikamat: 15th Waxing Day of Month 11
                     or 295[1-10] + 30[8.8] + 15[11] -1 = 339
        - Athikawan: 15th Waxing Day of Month 11
                     or 295[1-10] + 1[7] + 15[11] -1 = 310
        - Pakatimat: 15th Waxing Day of Month 11
                     or 295[1-10] + 15[11] -1 = 309

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Ok Phansa.
        '''
    def boun_suang_heua_date(self, year: int) -> date | None:
        '''
        Calculate the estimated Gregorian date of Ok Boun Suang Huea.
        If the Gregorian year input is invalid, this will outputs None instead.

        Boun Suang Huea Nakhone Luang Prabang, also known as "Vientiane Boat Racing Festival".
        This coincides with the 1st Waning Day of Month 11 in Thai Lunar Calendar.

        To calculate, we use use the following time delta:
        - Athikamat: 1st Waning Day of Month 11
                     or 295[1-10] + 30[8.8] + 16[11] -1 = 340
        - Athikawan: 1st Waning Day of Month 11
                     or 295[1-10] + 1[7] + 16[11] -1 = 311
        - Pakatimat: 1st Waning Day of Month 11
                     or 295[1-10] + 16[11] -1 = 310

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Boun Suang Huea.
        '''
    def loy_krathong_date(self, year: int) -> date | None:
        '''
        Calculate the estimated Gregorian date of Loy Krathong.
        If the Gregorian year input is invalid, this will outputs None instead.

        Also known as "Boun That Louang" and "Bon Om Touk".
        This coincides with the 15th Waxing Day of Month 12 in Thai Lunar Calendar.

        To calculate, we use use the following time delta:
        - Athikamat: 15th Waxing Day of Month 12
                     or 324[1-11] + 30[8.8] + 15[11] -1 = 368
        - Athikawan: 15th Waxing Day of Month 12
                     or 324[1-11] + 1[7] + 15[11] -1 = 339
        - Pakatimat: 15th Waxing Day of Month 12
                     or 324[1-11] + 15[11] -1 = 338

        :param year:
            The Gregorian year.

        :return:
            Estimated Gregorian date of Loy Krathong.
        '''
