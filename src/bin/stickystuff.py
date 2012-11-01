LANGS=("en", "it")
ads={}
ads["referral"]=["""<script type="text/javascript"><!--
google_ad_client = "pub-0988154404168132";
google_ad_width = 120;
google_ad_height = 60;
google_ad_format = "120x60_as";
google_cpa_choice = "CAEQABAAEAAQABoI_bmZ7iNYCIkow8b3cyic0Op-KNG593Mo6LK6iwE";
//-->
</script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>""", """<div width=120 height=160>Referral 120x160</div>"""]

ads["slimbanner"]=["""
<script type="text/javascript"><!--
google_ad_client = "pub-0988154404168132";
google_ad_width = 728;
google_ad_height = 15;
google_ad_format = "728x15_0ads_al";
google_color_bg = "000000";
google_color_link = "FFFFFF";
google_color_text = "FFFFFF";
google_ad_channel = "";
google_color_border = "000000";
//-->
</script>
<script type="text/javascript"
  src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>""", "<div width=728 height=15>Referral 728x15</div>"]

ads["skyscraper"]=["""<script type="text/javascript"><!--
google_ad_client = "pub-0988154404168132";
google_ad_width = 160;
google_ad_height = 600;
google_ad_format = "160x600_as";
google_ad_type = "text_image";
google_ad_channel = "";
google_color_border = "FFFFFF";
google_color_bg = "FFFFFF";
google_color_link = "336699";
google_color_text = "000000";
google_color_url = "88FF88";
google_ui_features = "rc:0";
//-->
</script>
<script type="text/javascript"
  src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
""","<div width=160 height=600>Referral 160x600</div>"]

ads["fatbanner"]=["""<script type="text/javascript"><!--
google_ad_client = "pub-0988154404168132";
google_ad_width = 728;
google_ad_height = 90;
google_ad_format = "728x90_as";
google_ad_type = "text_image";
google_ad_channel = "";
google_ui_features = "rc:0";
//-->
</script>
<script type="text/javascript"
  src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>""","<div width=728 height=90>Referral 728x90</div>"]

GOOGLE_SEARCH_ITA="""<!-- SiteSearch Google -->
<form method="get" action="http://www.google.it/custom" target="google_window">
<input type="radio" name="sitesearch" value="" checked id="ss0"></input>
<label for="ss0" title="Ricerca nel Web">Web</label>
<input type="radio" name="sitesearch" value="darkmoon.altervista.org" id="ss1"></input>
<label for="ss1" title="Cerca darkmoon.altervista.org">darkmoon</label>
<input type="hidden" name="client" value="pub-0988154404168132"></input>
<input type="hidden" name="forid" value="1"></input>
<input type="hidden" name="ie" value="ISO-8859-1"></input>
<input type="hidden" name="oe" value="ISO-8859-1"></input>
<input type="hidden" name="cof" value="GALT:#008000;GL:1;DIV:#224466;VLC:663399;AH:center;BGC:FFFFFF;LBGC:224466;ALC:0000FF;LC:0000FF;T:000000;GFNT:0000FF;GIMP:0000FF;FORID:1"></input>
<input type="hidden" name="hl" value="it"></input>
<input type="hidden" name="domains" value="darkmoon.altervista.org"></input>
<label for="sbi" style="display: none">Inserisci i termini di ricerca</label>
<input type="text" name="q" size="31" maxlength="255" value="" id="sbi"></input>
<label for="sbb" style="display: none">Invia modulo di ricerca</label>
<input type="submit" name="sa" value="Google" id="sbb"></input>
</form>
<!-- SiteSearch Google -->
"""

GOOGLE_SEARCH_UK="""
<!-- SiteSearch Google -->
<form method="get" action="http://www.google.it/custom" target="google_window">
<table border="0" bgcolor="#ffffff">
<tr><td nowrap="nowrap" valign="top" align="left" height="32">

</td>
<td nowrap="nowrap">
<input type="hidden" name="domains" value="darkmoon.altervista.org"></input>
<label for="sbi" style="display: none">Enter your search terms</label>
<input type="text" name="q" size="31" maxlength="255" value="" id="sbi"></input>
<label for="sbb" style="display: none">Submit search form</label>
<input type="submit" name="sa" value="Google Search" id="sbb"></input>
</td></tr>
<tr>
<td>&nbsp;</td>
<td nowrap="nowrap">
<table>
<tr>
<td>
<input type="radio" name="sitesearch" value="" checked id="ss0"></input>
<label for="ss0" title="Search the Web"><font size="-1" color="#000000">Web</font></label></td>
<td>
<input type="radio" name="sitesearch" value="darkmoon.altervista.org" id="ss1"></input>
<label for="ss1" title="Search darkmoon.altervista.org"><font size="-1" color="#000000">darkmoon.altervista.org</font></label></td>
</tr>
</table>
<input type="hidden" name="client" value="pub-0988154404168132"></input>
<input type="hidden" name="forid" value="1"></input>
<input type="hidden" name="ie" value="ISO-8859-1"></input>
<input type="hidden" name="oe" value="ISO-8859-1"></input>
<input type="hidden" name="cof" value="GALT:#008000;GL:1;DIV:#224466;VLC:663399;AH:center;BGC:FFFFFF;LBGC:224466;ALC:0000FF;LC:0000FF;T:000000;GFNT:0000FF;GIMP:0000FF;FORID:1"></input>
<input type="hidden" name="hl" value="en"></input>
</td></tr></table>
</form>
<!-- SiteSearch Google -->
"""

ANALYTICS="""
<script src="http://www.google-analytics.com/urchin.js" type="text/javascript">
</script>
<script type="text/javascript">
_uacct = "UA-2587939-2";
urchinTracker();
</script>
"""

SKYPE="""
<!--
Skype 'My status' button
http://www.skype.com/go/skypebuttons
-->
<script type="text/javascript" src="http://download.skype.com/share/skypebuttons/js/skypeCheck.js"></script>
<a href="skype:alepisa?call"><img src="http://mystatus.skype.com/smallclassic/alepisa" style="border: none;" width="114" height="20" alt="My status" /></a>
"""
