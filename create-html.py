#!/usr/bin/python

out_filename = "index.html"
page_title = "gmargari @ github.io"

pages = [
# First page is a special page that describes rest pages. It has fewer fields
# than other pages.
{
    "id"     : "all-pages", 
    "title"  : "Not-So-Usefull Pages",
    "text"   : """A collection of various pages I have created mostly for fun.
               All of them are hosted in <a href="https://github.com/gmargari/">github</a>,
               i.e., their html code and the code required to produce some
               of them is open source."""
},
{
    "id"     : "famous-quotes", 
    "title"  : "Famous Quotes",
    "text"   : "An image slider with more than 1000 famous quotes, as translated from English to Greek by Bing Translator.",
    "urlsuf" : "quotes/",
    "extra"  : "http://github.com/gmargari/bing-translated-quotes/",
    "image"  : "famous-quotes.jpeg"
},
{
    "id"     : "serres",
    "title"  : "Serres",
    "text"   : "Count the number of times the word \"SERRES\" appears in an image.",
    "urlsuf" : "serres/",
    "extra"  : "http://github.com/gmargari/serres/",
    "image"  : "serres.jpeg"
},
{
    "id"     : "kairos",
    "title"  : "Ioannina Weather Forecast",
    "text"   : "Accurately predict the weather in Ioannina city for any future day.",
    "urlsuf" : "kairos/",
    "image"  : "kairos.jpeg"
},
]



#===============================================================================
# addHtmlHeader()
#===============================================================================
def addHtmlHeader(outFile):
    html_header = """<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>{:s}</title>

    <link href="css/bootstrap.3.2.0.min.css" rel="stylesheet">
    <link href="css/landing-page.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="font-awesome-4.1.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>
"""
    outFile.write(html_header.format(page_title))

#===============================================================================
# addHeader()
#===============================================================================
def addHeader(outFile):

    header = """
    <!-- Header -->
    <div class="intro-header">

        <div class="container">

            <div class="row">
                <div class="col-lg-12">
                    <div class="intro-message">
                        <h1>gmargari</h1>
                        <hr class="intro-spacer">

                        <hr class="intro-divider">

                        <h3>Serious profile</h3>
                        <hr class="intro-spacer">
                        <ul class="list-inline intro-social-buttons">
                            <li>
                                <a href="https://www.linkedin.com/in/gmargari" class="btn btn-default btn-lg">
                                  <i class="fa fa-linkedin fa-fw"></i> <span class="network-name">&nbsp;LinkedIn</span>
                                </a>
                            </li>
                            <li>
                                <a href="https://github.com/gmargari/" class="btn btn-default btn-lg">
                                  <i class="fa fa-github fa-fw"></i> <span class="network-name">&nbsp;Github</span>
                                </a>
                            </li>
                            <li>
                                <a href="http://cs.uoi.gr/~gmargari/" class="btn btn-default btn-lg">
                                  <i class="fa fa-asterisk fa-fw"></i> <span class="network-name">&nbsp;cs page</span>
                                </a>
                            </li>
                        </ul>

                        <hr class="intro-divider">

                        <h3>*Ahem* Social profile</h3>
                        <hr class="intro-spacer">
                        <ul class="list-inline intro-social-buttons">
                            <li>
                                <a href="https://www.facebook.com/gmargari" class="btn btn-default btn-lg">
                                  <i class="fa fa-facebook fa-fw"></i> <span class="network-name">&nbsp;Facebook</span>
                                </a>
                            </li>
                            <li>
                                <a href="https://gmargari.wordpress.com/" class="btn btn-default btn-lg">
                                  <i class="fa fa-wordpress fa-fw"></i> <span class="network-name">&nbsp;Wordpress</span>
                                </a>
                            </li>
                            <li>
                                <a href="http://gmargari.tumblr.com/" class="btn btn-default btn-lg">
                                  <i class="fa fa-tumblr fa-fw"></i> <span class="network-name">&nbsp;Tumblr</span>
                                </a>
                            </li>
                        </ul>

                    </div>
                </div>
            </div>

        </div>
        <!-- /.container -->

    </div>
    <!-- /.intro-header -->
"""
    outFile.write(header)

#===============================================================================
# addContent()
#===============================================================================
def addContent(outFile):

    pages_header = """
    <!-- Page Content -->

    <div class="content-section-a" id="{:s}">
        <div class="container">
            <div class="row">
                <div class="col-lg-5 col-sm-6">
                    <div class="clearfix"></div>
                    <h2 class="section-heading">{:s}</h2>
                    <p class="lead">
                        {:s}
                    </p>
                </div>
                <div class="col-lg-5 col-lg-offset-2 col-sm-6">
                    {:s}
                </div>
            </div>
        </div>
    </div>
    <!-- /.content-section-a -->
"""

    page_link_template = "<a href='#{:s}' class='btn btn-primary'>{:s}</a>"

    pages_template = """
    <div class="content-section-{:s}" id="{:s}">
        <div class="container">
            <div class="row">
                <div class="{:s}">
                    <div class="clearfix"></div>
                    <h2 class="section-heading">{:s}</h2>
                    <p class="lead">
                        {:s}
                    </p>
                        {:s}
                </div>
                <div class="{:s}">
                    <img class="img-responsive img-thumbnail" src="img/{:s}" alt="">
                </div>
            </div>
        </div>
    </div>
    <!-- /.content-section-{:s} -->
"""

    view_link_template =   "<a href='{:s}' class='btn btn-info'><span class='glyphicon glyphicon-eye-open'></span> &nbsp;View</a>"
    source_link_template = "<a href='{:s}' class='btn btn-info'><span class='glyphicon glyphicon-pencil'></span> &nbsp;Source</a>"
    extra_link_template =  "<a href='{:s}' class='btn btn-info'><span class='glyphicon glyphicon-cog'></span> &nbsp;Extra code</a>"
    back_link_template =   "<a href='{:s}' class='btn btn-info'><span class='glyphicon glyphicon-arrow-up'></span> &nbsp;Back to all pages</a>"

    links = ""
    for i in range(1, len(pages)):
        links += page_link_template.format(pages[i]["id"], pages[i]["title"]) + " "
    outFile.write(pages_header.format(pages[0]["id"], pages[0]["title"], pages[0]["text"], links))

    for i in range(1, len(pages)):
        p = pages[i]
        if (i % 2 == 0):
            class1 = "a"
            class2 = "col-lg-5 col-sm-6"
            class3 = "col-lg-5 col-lg-offset-2 col-sm-6"
        else:
            class1 = "b"
            class2 = "col-lg-5 col-lg-offset-1 col-sm-push-6 col-sm-6"
            class3 = "col-lg-5 col-sm-pull-6 col-sm-6"

        links = view_link_template.format("http://gmargari.github.io/" + pages[i]["urlsuf"]) + " "
        links += source_link_template.format("http://github.com/gmargari/gmargari.github.io/tree/master/" + pages[i]["urlsuf"]) + " "
        if ("extra" in pages[i] and pages[i]["extra"] != ""): 
            links += extra_link_template.format(pages[i]["extra"]) + " "
        links += back_link_template.format("#" + pages[0]["id"]) + " "

        outFile.write(pages_template.format(class1, p["id"], class2, 
          p["title"], p["text"], links, class3, p["image"], class1))

#===============================================================================
# addBanner()
#===============================================================================
def addBanner(outFile):

    banner = """
    <div class="banner">
        <div class="container">
            <div class="row">
                <div class="col-lg-6">
                    <h2>Express your admiration:</h2>
                </div>
                <div class="col-lg-6" style="text-align:center">
                    <script type="text/javascript">
                    <!--
                    document.write('<a href="mailto:&#103;&#109;&#97;&#114;&#103;&#97;&#114;&#105;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;" class="btn btn-default btn-lg"><span class="glyphicon glyphicon-envelope"></span><span class="network-name"> &nbsp;Email me</span></a>')
                    // -->
                    </script>
                </div>
            </div>

        </div>
        <!-- /.container -->

    </div>
    <!-- /.banner -->
"""
    outFile.write(banner)

#===============================================================================
# addFooter()
#===============================================================================
def addFooter(outFile):

    footer = """
    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <!--
                    <ul class="list-inline">
                        <li>
                            <a href="#home">Home</a>
                        </li>
                        <li class="footer-menu-divider">&sdot;</li>
                        <li>
                            <a href="#about">About</a>
                        </li>
                        <li class="footer-menu-divider">&sdot;</li>
                        <li>
                            <a href="#services">Services</a>
                        </li>
                        <li class="footer-menu-divider">&sdot;</li>
                        <li>
                            <a href="#contact">Contact</a>
                        </li>
                    </ul>
                    -->
                    <p class="copyright text-muted small">
                      Work licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
                      Creative Commons Attribution 4.0 International License</a>.
                      Page template is <a href="http://startbootstrap.com/template-overviews/landing-page/">Landing Page</a>.
                      Page source can be found <a href="http://github.com/gmargari/gmargari.github.io/">here</a>.
                    </p>
                </div>
            </div>
        </div>
    </footer>
"""
    outFile.write(footer)

#===============================================================================
# addHtmlFooter()
#===============================================================================
def addHtmlFooter(outFile):

    html_footer = """
    <script src="js/jquery.1.11.1.min.js"></script>
    <script src="js/bootstrap.3.2.0.min.js"></script>
</body>

</html>
"""
    outFile.write(html_footer)

#==============================================================================
# main()
#==============================================================================
def main():
    with open(out_filename, "w") as outFile:
    #        outFile.write(header.format(image_prefix + "/images/quote-0.jpg", file_lines[0].split("#")[0]))
        addHtmlHeader(outFile)
        addHeader(outFile)
        addContent(outFile)
        addBanner(outFile)
        addFooter(outFile)
        addHtmlFooter(outFile)

if __name__ == "__main__":
    main()

