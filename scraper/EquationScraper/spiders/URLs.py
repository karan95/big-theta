import re

start_url_dict = { 'portals': ['https://en.wikipedia.org/wiki/Portal:Science/Categories_and_Main_topics',
                              'https://en.wikipedia.org/wiki/Portal:Computer_science', ],
                  'wikiprojects': [
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(0%E2%80%939)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(A)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(B)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(C)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(D)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(E)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(F)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(G)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(H)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(I)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(J)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(K)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(L)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(M)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(N)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(O)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(P)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(Q)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(R)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(S)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(T)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(U)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(V)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(W)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(X)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(Y)',
                      'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_(Z)'
                  ],
                  'articles': ['https://en.wikipedia.org/wiki/List_of_equations',
                               'https://en.wikipedia.org/wiki/Laws_of_science', ]}

start_urls_list = [url for url_list in start_url_dict.values() for url in url_list]

global_deny = [
    re.escape("https://en.wikipedia.org/wiki/Mathematical_Reviews"),
    re.escape("https://en.wikipedia.org/wiki/Wikipedia:Stub"),
    r"https://en[.]wikipedia[.]org/w/.*",
    re.escape(
        "https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License"),
    re.escape("https://en.wikipedia.org/wiki/Wikipedia:About"),
    re.escape("https://en.wikipedia.org/wiki/Wikipedia:General_disclaimer"),
    re.escape("https://en.wikipedia.org/wiki/Wikipedia:Contact_us"),
    re.escape("https://en.wikipedia.org/wiki/Main_Page"),
    re.escape("https://en.wikipedia.org/wiki/Portal:Contents"),
    re.escape("https://en.wikipedia.org/wiki/Portal:Featured_content"),
    re.escape("https://en.wikipedia.org/wiki/Portal:Current_events"),
    re.escape("https://en.wikipedia.org/wiki/Special:Random"),
    re.escape("https://en.wikipedia.org/wiki/Wikipedia:About"),
    re.escape("https://en.wikipedia.org/wiki/Wikipedia:Community_portal"),
    re.escape("https://en.wikipedia.org/wiki/Help:Contents"),
    re.escape("https://en.wikipedia.org/wiki/Special:RecentChanges"),
    re.escape("https://en.wikipedia.org/wiki/Wikipedia:Contact_us"),
    re.escape("https://en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard"),
    re.escape("https://en.wikipedia.org/wiki/Special:SpecialPages"),
    re.escape("https://en.wikipedia.org/wiki/Portal:Contents/Portals#Religion_and_belief_systems"),
    re.escape("https://en.wikipedia.org/wiki/Portal:Contents/Portals#History_and_events"),
    re.escape("https://en.wikipedia.org/wiki/Portal:Contents/Portals#Culture_and_the_arts"),
    re.escape("https://en.wikipedia.org/wiki/Portal:Contents/Portals#Geography_and_places"),
    re.escape("https://en.wikipedia.org/wiki/Portal:Contents/Portals#Society_and_social_sciences"),
    re.escape("https://en.wikipedia.org/wiki/Category:Featured_portals"),
    r"https://en[.]wikipedia[.]org/wiki/Talk.*",
    r"https://commons[.]wikimedia[.]org/wiki/Commons.*",
    re.escape("https://en.wikipedia.org/wiki/Special:MyTalk"),
    re.escape("https://en.wikipedia.org/wiki/Special:MyContributions"),
    re.escape("https://en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard"),
    # re.escape(""),
    # re.escape(""),
    # re.escape(""),
    # re.escape(""),
    # re.escape(""),
    # re.escape(""),
    # re.escape(""),
    # re.escape(""),
    # re.escape(""),
    # re.escape(""),
    # re.escape(""),
    # re.escape(""),
    # re.escape(""),

]
