import Media
import fresh_tomatoes
movie1=Media.Movie("The Silence Of The Lambs",
                      "boy and his toy comes into life",
                      "http://posterwire.com/wp-content/uploads/silence_of_the_lambs.jpg",
                      "https://youtu.be/RuX2MQeb8UM?t=9")
movie2=Media.Movie("The Pursuit Of Happyness",
                      "boy and his toy comes into life",
                      "https://tse3.mm.bing.net/th?id=OIP.T1lZ0f7N27mh_VXIHTlURwDIEs&pid=15.1&P=0&w=300&h=300",
                      "https://youtu.be/89Kq8SDyvfg?t=13")
movie3=Media.Movie("Angels And Demons",
                      "boy and his toy comes into life",
                      "https://tse4.mm.bing.net/th?id=OIP.vfHfQ0aglMjN7sDrMalJjQEsDw&pid=15.1&P=0&w=211&h=170",
                      "https://youtu.be/hkvqtBaigjY?t=9")
movie4=Media.Movie("The Wolf Of Wall Street",
                      "boy and his toy comes into life",
                      "https://tse1.mm.bing.net/th?id=OIP.TimA75q2nNkXS0GJFJc4YwEsEs&pid=15.1&P=0&w=300&h=300",
                      "https://youtu.be/iszwuX1AK6A?t=2")
movie5=Media.Movie("Theoy of EveryThing",
                      "boy and his toy comes into life",
                      "https://tse4.mm.bing.net/th?id=OIP._iVbp5WdJ0auo3rNGJL-LwEsDU&pid=15.1&P=0&w=236&h=168",
                      "https://youtu.be/Salz7uGp72c?t=1")
movie6=Media.Movie("Shawshank Redemption",
                      "boy and his toy comes into life",
                      "https://tse3.mm.bing.net/th?id=OIP.gDI432WYExnJXNXozKimGQEsDh&pid=15.1&P=0&w=210&h=159",
                      "https://youtu.be/NmzuHjWmXOc?t=37")
movie7=Media.Movie("Now U See Me",
                      "boy and his toy comes into life",
                      "https://tse3.mm.bing.net/th?id=OIP.fuqvbCx17SnaEpHIvLKR7wEsDh&pid=15.1&P=0&w=229&h=173",
                      "https://youtu.be/4OtM9j2lcUA?t=1")
movie8=Media.Movie("Tangled",
                      "boy and his toy comes into life",
                      "https://tse4.mm.bing.net/th?id=OIP.GKI3QvKIllonaG-A7DkZ_gDSEs&pid=15.1&P=0&w=300&h=300",
                      "https://youtu.be/JYKpIr1lSG0?t=4")
movie9=Media.Movie("Predestination",
                      "boy and his toy comes into life",
                      "https://tse3.mm.bing.net/th?id=OIP.qzAYvxPJAv6UnbROv--zWQDOEs&pid=15.1&P=0&w=300&h=300",
                      "https://youtu.be/-FcK_UiVV40?t=3")
movie10=Media.Movie("Frozen",
                      "boy and his toy comes into life",
                      "https://tse1.mm.bing.net/th?id=OIP.gG4lt3lu499LxkBQX2VlwgFNC7&pid=15.1&P=0&w=307&h=173",
                      "https://youtu.be/TbQm5doF_Uc?t=1")
movie11=Media.Movie("Fantastic Four",
                      "boy and his toy comes into life",
                      "http://media.comicbook.com/uploads1/2015/02/fantastic-four-2005-poster-121751.jpg",
                      "https://youtu.be/_rRoD28-WgU?t=2")
movie12=Media.Movie("Forest Grump",
                      "boy and his toy comes into life",
                      "https://tse2.mm.bing.net/th?id=OIP.A8BOBPCBu57-gd_3uE8v0wGECg&pid=15.1&P=0&w=377&h=156",
                      "https://youtu.be/uPIEn0M8su0?t=3")



movies=[movie1,movie2,movie3,movie4,movie5,movie6,movie7,movie8,movie9,movie10,movie11,movie12]
fresh_tomatoes.open_movies_page(movies)
