# -*- coding: utf-8-*-

def time(h,m):
    nat_time=""
    words=["zero","pierwsza","druga","trzecia","czwarta","piąta","szósta",
           "siódma","ósma","dziewiąta","dziesiąta","jedenasta","dwunasta",
           "trzynasta","czternasta","piętnasta","szesnasta","siedemnasta",
           "osiemnasta","dziewiętnasta","dwudziesta","dwudziestapierwsza",
           "dwudziestadruga","dwudziestatrzecia"]
    nat_time+=words[h]
    nat_time += " %s" % m
    return nat_time

def date(w,d,m,y):
    nat_date=""
    wwords=["poniedziałek","wtorek","środa","czwartek","piątek",
            "sobota","niedziela"]
    nat_date+=wwords[w]
    dwords=["pierwszego","drugiego","trzeciego","czwartego","piątego","szóstego",
            "siódmego","ósmego","dziewiątego","dziesiątego","jedenastego","dwunastego",
            "trzynastego","czternastego","piętnastego","szesnastego","siedemnastego",
            "osiemnastego","dziewiętnastego","dwudziestego","dwudziestegopierwszego",
            "dwudziestegodrugiego","dwudziestegotrzeciego","dwudziestegoczwartego",
            "dwudziesstegopiątego","dwudziestegoszóstego","dwudziestegosiódmego",
            "dwudziestegoósmego","dwudziestegodziewiątego","trzydziestego","trzydziestegopierwszego"]
    nat_date+=" " + dwords[d-1]
    mwords=["stycznia","lutego","marca","kwietnia","maja","czerwca","lipca",
            "sierpnia","września","października","listopada","grudnia"]
    nat_date+=" " + mwords[m-1]
    nat_date+= " %s" % y    
    return nat_date
    
   