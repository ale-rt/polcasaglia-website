#!/usr/bin/env python

"""USAGE:

OPTIONS:
    -h, -?, --help: obtain help

TODO:
"""
import sys, os, getopt, re, time
from stickystuff import *

TEST=0
# checks options
def checkopt():
    DOCTYPE=r'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">'
    flags={"DOCTYPE":DOCTYPE,
           "CSS": "style.css",
           "AUTHOR": "Darkmoon",
           "MAIL": "alessandro...pisa@@@gmail...com",
           }
    sopt='h?'
    lopt=['help']
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], sopt, lopt)
    except getopt.GetoptError:
        sys.stderr.write(__doc__)
    for opt, optarg in opts:
        if opt in ('-h', '-?', '--help'):
            sys.stdout.write(__doc__)
            sys.exit()
    return opts, args, flags

opts, args, flags=checkopt()

class Td(object):
    def __init__(self, text, cssclass, options=""):
        self.text=text
        self.cssclass=cssclass
        self.options=options

    def __str__(self):
        return '  <td class="%s" %s>\n   %s\n  </td>\n' % (self.cssclass, self.options, self.text)

class Tr(object):
    def __init__(self, tds, cssclass, options=""):
        self.text="".join(["%s" % td for td in tds])
        self.cssclass=cssclass
        self.options=options

    def __str__(self):
        """Returns in notime a well formated <tr> element given a td list"""
        return ' <tr class="%s" %s>\n%s </tr>\n' % (self.cssclass, self.options, self.text)

class Table(object):
    def __init__(self, trs, summary, cssclass, options=""):
        self.text="".join(["%s" % tr for tr in trs])
        self.summary=summary
        self.cssclass=cssclass
        self.options=options

    def __str__(self):
        """Returns in notime a well formated <table> element given a tr list"""
        return '<table summary="%s" class="%s" %s>\n%s </table>\n' % (self.summary, self.cssclass, self.options, self.text)

class A(object):
    def __init__(self, text, url, cssclass, options=""):
        self.text=text
        self.url=url
        self.cssclass=cssclass
        self.options=options

    def __str__(self):
        """Returns in notime a well formated <table> element given a tr list"""
        return '<a href="%s" class="%s" %s>%s</a>' % (self.url, self.cssclass, self.options, self.text)


class Page(object):
    def __init__(self, filename):
        # reliminar check about the file existency
        if not os.path.isfile(filename):
            sys.stderr.write("I can process only existing files!!!\n")
        # files to process are contained in the src directory
        # using standard paths the filename argument should have the form
        # "../src/WHATEVER"
        self.src=filename
        self.lines=file(self.src).read()
        # standard prepath=".."
        # standard name="WHATEVER"
        self.prepath, self.name = self.src.split("/src/")
        # divided the name in a list: with N directory plus the last element
        # which is the filename
        self.name_stripped=self.name.split("/")
        # to reach the base directory we need to go back the number of dirs in
        # the list plus 1, i.e. the length of the list
        self.depth=len(self.name_stripped)
        self.backstring="../"*self.depth
        # standard css file [not used for most of the stuff]
        self.css=self.backstring+"css/"+flags["CSS"]
        self.doctype=flags["DOCTYPE"]
        self.parse_header()
        self.parse_text()
        self.parse_footer()
        # Calculates the day in which the file was last edited and saves in
        # human readable form
        self.mtime=os.stat(self.src).st_mtime
        self.mtime_string=time.strftime("%d %h %Y", time.localtime(self.mtime))
        self.time_string=time.strftime("%d %h %Y")

    def template(self):
        """Standard template for a nice start!
        ou need to replace the html text in the body!
        """
        output=file(self.src, 'w').write
        output("""%s
<html>
<head>
<title>CHANGE ME</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-15">
<link rel="STYLESHEET" href="%s" type="text/css">
</head>
<body>

<!--it-->
    <p>
    Pagina non disponibile in questa lingua!
    <FORM><INPUT TYPE="button" VALUE="Indietro" onClick="history.go(-1);return true;"> </FORM>
    </p>
<!--/it-->

<!--en-->
    <p>
    Page not available in this language!
    <FORM><INPUT TYPE="button" VALUE="Back" onClick="history.go(-1);return true;"> </FORM>
    </p>
<!--/en-->

</body>
</html>
""" % (self.doctype, self.css))

    def append_subfiles(self, di, lines, lang):
        """Crappy function to add submenus to site navigator

        lines are the lines of the site navigator table!
        TODO: polish code!!!
        """
        if lang=="en":lang_index=1
        elif lang=="it":lang_index=2
        try:
            #if di[0] in self.name_stripped:
            for key in TREE.keys():
                if di[0]==key and di[0] in self.name_stripped:
                    deco=["&nbsp;&nbsp;|-&nbsp;" for i in range(len(TREE[key])-1)]
                    deco.append("&nbsp;&nbsp;`-&nbsp;")
                    for d, fi in zip(deco, TREE[key]):
                        bough="%s%s" % (d,fi[lang_index])
                        path="%s%s/%s/%s" % (self.backstring, lang, di[0], fi[0])
                        lines.append("%s %s" % (path, bough))
        except IndexError:
            pass
        return lines

    def append_navigator(self, lines, lang):
        lines.append("section Site Navigator")
        lines.append("index.html Home")
        lines.append("album.html Album")
        lines.append("marcatori.html Classifica marcatori")
        lines.append("mappe.html Mappe")
        lines.append("meteo.html Meteo")
        return lines

    def append_links(self, lines, lang):
        """Appends a section containing external links link"""
        lines.append("verbatim &nbsp;")
        lines.append("section Links")
        lines.append("external http://polcasaglia.blogspot.com Blog")
        lines.append("external http://www.uisp-fe.it/calcio.php UISP" )
        lines.append("verbatim &nbsp;")
        return lines

    def append_misc(self, lines, lang):
        """Appends a section containing miscellaneous stuff links link"""
        if lang=="en":
            lines.append("section Misc")
            lines.append("%s%s/credits.html %s" % (self.backstring, lang, "Credits"))
            lines.append("%s%s/search.html %s" % (self.backstring, lang, "Search"))
            lines.append("external %s/old/index.html %s" % (self.backstring, "Ye olde Darkmoon ;("))
            lines.append("verbatim &nbsp;")
        elif lang=="it":
            lines.append("section Misc")
            lines.append("%s%s/credits.html %s" % (self.backstring, lang, "Ringraziamenti"))
            lines.append("%s%s/search.html %s" % (self.backstring, lang, "Cerca"))
            lines.append("external %s/old/index.html %s" % (self.backstring, "Il vecchio Darkmoon ;("))
            lines.append("verbatim &nbsp;")
        return lines

    def append_contacts(self, lines, lang):
        """Appends a section containing miscellaneous stuff links link"""
        if lang=="en":
            lines.append("section Contacts")
        elif lang=="it":
            lines.append("section Contatti")
        lines.append("mailto://%s e-mail" % flags['MAIL'])
        lines.append("verbatim %s" % SKYPE)
        lines.append("verbatim &nbsp;")
        return lines

    def append_lastupdate(self, lines, lang):
        """Append last update information"""
        lines.append("section Last update")
        lines.append('verbatim <i class="lastupdate">pagina: %s</i>' % self.mtime_string)
        lines.append('verbatim <i class="lastupdate">sito: %s</i>' % self.time_string)
        return lines

    def navside_lines(self, lang):
        """Lines for building the table of the side with the site navigator"""
        lines=[]
        self.append_navigator(lines, lang)
        self.append_links(lines, lang)
        # self.append_misc(lines, lang)
        self.append_contacts(lines, lang)
        self.append_lastupdate(lines, lang)
        return lines

    def parse_header(self):
        """Extracts the header of the source page"""
        bodystart=re.compile(r"<body>", re.IGNORECASE).search(self.lines).span()[1]
        oldheader=self.lines[0:bodystart]
        start=re.compile("<title>", re.IGNORECASE).search(oldheader).span()[1]
        finish=re.compile("</title>", re.IGNORECASE).search(oldheader).span()[0]
        titles=oldheader[start:finish].split("--")
        # Duplicate if needed
        if len(titles)==1: titles.append(titles[0])
        self.title, self.header= {}, {}
        for i, lang in enumerate(LANGS):
            self.title[lang]=titles[i]
            self.header[lang]="%s%s%s" % (oldheader[:start], self.title[lang], oldheader[finish:],)

    def parse_text(self):
        """Extracts the part of the correct language!"""
        self.text={}
        for i, lang in enumerate(LANGS):
            text=file(self.src).read()
            self.text[lang]=""
            extracted, finish = "", 0
            start_string, stop_string = r"<!--%s-->" % lang, r"<!--/%s-->" % lang
            # Iterates to check multiple blocks of text within the file!
            # Pay attention to infinite loops!
            # AttributeError exception raised when no more blocks to extract exist
            while True:
                try:
                    start=re.compile(start_string, re.IGNORECASE).search(text).span()[1]
                    finish=re.compile(stop_string, re.IGNORECASE).search(text).span()[0]
                    extracted+=text[start:finish]
                    text=text[finish+1:]
                except AttributeError:
                    break
            self.text[lang]+=extracted

    def parse_footer(self):
        """Extracts the header of the source page"""
        lines=self.lines
        bodyfinish=re.compile(r"</body>", re.IGNORECASE).search(lines).span()[0]
        self.footer=lines[bodyfinish:]

    def frame_body(self, lang):
        """Formats the central table"""
        return self.text[lang]
        toptds=(Td('', "frame-nw", 'width=8'),
                Td("", "frame-n"),
                Td("", "frame-ne", 'width=8'),
               )
        midtds=(Td("", "frame-w", 'width=8'),
                Td(body, "frame-c"),
                Td("", "frame-e", 'width=8'),
               )
        bottds=(Td("", "frame-sw", 'width=8'),
                Td("", "frame-s"),
                Td("", "frame-se", 'width=8'),
               )
        trs=(Tr(toptds, "frame",),
             Tr(midtds, "frame"),
             Tr(bottds, "frame",),
            )
        return Table(trs, "Page", "frame", 'width=480 cellspacing=0 cellpadding=0')

    def get_translation(self, lang):
        """Prepares the translation magic button"""
        if lang=="it":
            url=self.backstring+"en/"+self.name
            image=self.backstring+"img/uk.png"
            alttext='English version'
        elif lang=="en":
            url=self.backstring+"it/"+self.name
            image=self.backstring+"img/it.png"
            alttext='Italian version'
        img='<img src="%s" height="15" alt="%s"><br>%s' % (image, alttext,alttext, )
        a=A(img, url, "translation")
        return str(a)

    def google_search(self, lang):
        """Returns the websearch stuff"""
        return GOOGLE_SEARCH_ITA

    def get_corner_left(self, lang):
        """Returns the left top corner of the page, with clickable logo that
        points towards the homepage."""
        url="%s/%s/index.html" % (self.backstring, lang)
        img='<img class="corner-left" alt="Corner image" border="0" src="%simg/corner-left.png">' % self.backstring
        a=A(img, url, "corner")
        return Td(str(a), "corner-left",)

    def comb_side(self, line, lang):
        """Transforms the line in a <td> element according to some standars keywords."""
        line=line.split()
        if len(line)!=0:
            if line[0]==self.name:
                tds=(Td('%s' % (" ".join(line[1:])), "sidethispage"),)
            elif line[0]=="verbatim":
                tds=(Td('%s' % ("\n".join(line[1:])), "side"),)
            elif line[0]=="section":
                tds=(Td('%s' % (" ".join(line[1:])), "sidesection"),)
            elif line[0]=="external":
                text=" ".join(line[2:])
                url=line[1]
                a=A(text, url, "side", 'target="_blank"')
                tds=(Td(str(a), "side"),)
            else:
                text=" ".join(line[1:])
                url=line[0]
                a=A(text, url, "side")
                tds=(Td(str(a), "side"),)
            return Tr(tds, "side")

    def get_adsside(self, lang):
        """Ads that have to be put on the side column"""
        tds=[]
        tds.append(Td('<img src="logopolcasaglia.jpg" width="100" height="119" alt="[logo]">', "logo"))
        tds.append(Td(ads["referral"][TEST], "referral"))
        tds.append(Td(ads["skyscraper"][TEST], "skyscraper"))
        trs=[Tr((td,), td.cssclass) for td in tds]
        return Table(trs, "adsside", "ads table", 'cellspacing=0 cellpadding=0 align="center"')

    def get_navside(self, lang):
        """Formats the site navigation table"""
        trs=[self.comb_side(line, lang) for line in self.navside_lines(lang)]
        trs=[tr for tr in trs if tr is not None]
        return Table(trs, "navside", "side", 'width=200 cellspacing=0 cellpadding=0 align="center"')

    def get_top_table(self, lang):
        """Formats the top table with google search and translation"""
        gsearch_td=Td(self.google_search(lang), "")
        translate_td=Td(self.get_translation(lang), "top")
        trs=(Tr((gsearch_td, translate_td), "top", 'align="center"'),)
        return Table(trs, "Top", "top",  'align="right" cellspacing=0 cellpadding=0"')

    def remake_body(self, lang):
        """Returns the formatted page as a table!
        It needs only an header and footer with the correct html preamble and conclusion.
        """
        # advertisement first...
        # top
        hat=Tr((Td('<h1 class="hat">Polisportiva&nbsp;Casaglia</h1>', 'top', 'colspan=3 align="center"'),
               ), "hat", 'valign="center"'),
        hat=Table((hat,), "hat", "hat", ' align="center"')
        hat=Td(hat, "hat", "colspan=3")
        hat=Tr((hat,), "hat")
        slimbanner=Td(ads["slimbanner"][TEST], "slimbanner", 'align="center" colspan=3')
        slimbannertr=Tr((slimbanner, ), "slimbanner")
        # bottom
        # The top table
        # top_table=Td(self.get_top_table(lang), "toptable", 'height="40" colspan=2')
        # toptr=self.tr((self.get_corner_left(lang), top_table, self.get_corner_right(lang)), "body")
        # toptr=Tr((self.get_corner_left(lang), top_table), "body")
        # Then the body table
        navside=Td(self.get_navside(lang), "sidetable", 'valign="top"')
        center=Td(self.frame_body(lang), "bodytable", 'align="center" valign="top" width=440')
        adsside=Td(self.get_adsside(lang), "adsensetable", 'align="center" valign="top"')
        midtr=Tr((adsside,center,navside,), "mid")
        table=Table((hat, slimbannertr, midtr,), "Banner", "main", 'cellspacing=0 cellpadding=0')
        return """<div align="center">%s</div>""" % table

    def ap2html_lang(self, lang):
        apbody=self.remake_body(lang)
        compiled=self.header[lang]+apbody+ANALYTICS+self.footer
        filename="%s/%s/%s" % (self.prepath, lang, self.name)
        file(filename, 'w').write(compiled)

    def ap2html(self):
        self.ap2html_lang('it')

if __name__=='__main__':
    # Import Psyco if available
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    # ...your code here...
    for arg in args:
        page=Page(arg)
        page.ap2html()