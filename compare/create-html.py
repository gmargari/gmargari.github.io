#!/usr/bin/python
# -*- coding: utf-8 -*-

out_filename = "index.html"
page_title = "Comparisons"

comparisons = [
{
    "item1"  : "Φίλιππος Πλιάτσικας",
    "img1"   : "pliatsikas.jpg",
    "item2"  : "Μία Πέτρα",
    "img2"   : "stone.jpg",
    "questions" : [
            [ "Μπορεί να συνθέσει αξιόλογη μουσική", "n", "n" ],
            [ "Έχει ωραία φωνή", "n", "n" ],
            [ "Έχει ενεπνεύσει τη δημιουργία αξιόλογων μουσικών ειδών", "n", "y", "c2: Rock 'n' Roll, Stoner" ],
            [ "Μπορεί να χρησιμοποιηθεί για λιθοβολισμό", "n", "y" ],
            [ "Νικάει το ψαλίδι", "n", "y" ],
            [ "Μπορείς να χρησιμοποιήσεις φωτογραφία του/της για να ταΐσεις ένα παιδί", "y", "n" ],
        ]
},
]



#===============================================================================
# addHtmlHeader()
#===============================================================================
def addHtmlHeader(outFile):
    html_header = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">  
    <title>{:s}</title>
    <script type="text/javascript" src="../js/jquery.1.11.1.min.js"></script>
    <script type="text/javascript" src="../js/bootstrap.3.2.0.min.js"></script>
    <link rel="stylesheet" type="text/css" href="../css/bootstrap.3.2.0.min.css">
    <!-- Google Analytics -->
    {:s}
    
    {:s}

    {:s}
</head>
<body style="background-color: #eeeeee">
"""
    google_analytics = """<script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
      ga('create', 'UA-53994042-1', 'auto');
      ga('send', 'pageview');
    </script>"""

    extra_script = """<script>
       $(function(){
          $(".prev-slide").click(function(){
             $("#myCarousel").carousel('prev');
          });
          $(".next-slide").click(function(){
             $("#myCarousel").carousel('next');
          });
          // Start carousel paused
          $("#myCarousel").carousel('pause');

          // Go to next/previous carousel item using arrow keys
          $(document).keydown(function(e) {
              switch(e.which) {
                  case 37: // left
                  $("#myCarousel").carousel('prev');
                  break;

                  case 39: // right
                  $("#myCarousel").carousel('next');
                  break;

                  default: return; // exit this handler for other keys
              }
              e.preventDefault(); // prevent the default action (scroll / move caret)
          });
       });
    </script>"""

    extra_style = """<style>
        .glyphicon-ok {
            color: #00aa00;
        }
        .glyphicon-remove {
            color: #aa0000;
        }
        .col-xs-6 {
            text-align: left;
        }
        td.qimage {
            text-align: center;
        }
        td.qmark {
            text-align: center;
        }
        td.qnote {
            text-align: left;
        }
        .borderless tbody tr td, .borderless thead tr th {
            border: none;
        }
        table.borderless {
            margin: 0px;
        }
        .text-middle {
            vertical-align: middle;
        }
        .panel {
            width: 600px;
            margin-left: auto;
            margin-right: auto;
            margin-top: 10px;
            margin-bottom: 0px;
        }
        .panel-title {
            font-size: 16px;
            text-align: center;
        }
        .table-condensed {
            margin-bottom: 0px;
        }
    </style>"""
    
    outFile.write(html_header.format(page_title, google_analytics, extra_script, extra_style))

#===============================================================================
# addContent()
#===============================================================================
def addContent(outFile):

    carousel_header = """
    <!-- Carousel -->
    <div id="myCarousel" class="carousel slide">
        <div class="carousel-inner">"""

    carousel_item_header = """

            <!-- Carousel item -->
            <div class="item{:s}">"""

    carousel_item_footer = """
            </div>
            <!-- /Carousel item -->"""

    carousel_footer = """
        </div>
    </div>
    <!-- /Carousel -->
"""
        
    panel_template = """

                <!-- Panel -->
                <div class="panel panel-primary">
                    <!-- Panel header -->
                    <div class="panel-heading">
                        <div class="row">
                            <div class="col-xs-2"><a class="btn btn-default prev-slide">Previous</a></div>
                            <div class="col-xs-8"><h4 class="text-center">{:s}</h4></div>
                            <div class="col-xs-2"><a class="btn btn-default next-slide">Next</a></div>
                        </div>
                    </div>
                    <!-- Panel body -->
                    <div class="panel-body">
                    
                        <!-- Header table with names and images -->
                        <table class="table borderless table-condensed">
                            <tbody>
                                <tr>
                                    <td class="col-xs-6"></td>
                                    <td class="col-xs-3 qimage">
                                        <img class="img-responsive img-thumbnail" style="margin: 0px;" src="img/{:s}"><br>
                                        <h5>{:s}</h5>
                                    </td>
                                    <td class="col-xs-3 qimage">
                                        <img class="img-responsive img-thumbnail" style="margin: 0px;" src="img/{:s}"><br>
                                        <h5>{:s}</h5>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <!-- Basic table with comparison questions -->
                        <table class="table table-hover table-condensed">
                            <tbody>{:s}
                            </tbody>
                        </table>
                    </div>{:s}
                </div>
                <!-- /Panel -->
"""

    table_row_template = """
                                <tr>
                                    <td class="col-xs-6">{:s}:</td>
                                    <td class="col-xs-1"></td>
                                    <td class="col-xs-1 qmark" style="vertical-align: middle">{:s}</td>
                                    <td class="col-xs-1 qnote" style="vertical-align: middle">{:s}</td>
                                    <td class="col-xs-1"></td>
                                    <td class="col-xs-1 qmark" style="vertical-align: middle">{:s}</td>
                                    <td class="col-xs-1 qnote" style="vertical-align: middle">{:s}</td>
                                </tr>"""

    panel_footer_template = """
                <!-- Panel footer -->
                <div class="panel-footer">
                    <small>
                    Σημειώσεις:{:s}
                    </small>
                </div>
"""

    y_icon = '<span class="glyphicon glyphicon-ok"></span>'
    n_icon = '<span class="glyphicon glyphicon-remove"></span>'
    u_icon = '<b style="color: #666666;">?</b>'
    
    outFile.write(carousel_header)
    
    carousel_items = 0
    for c in comparisons:
        if (carousel_items == 0):
            outFile.write(carousel_item_header.format(" active"))
        else:
            outFile.write(carousel_item_header.format(""))
        
        panel_title = c["item1"] + " vs. " + c["item2"];
        title1 = c["item1"]
        title2 = c["item2"]
        image1 = c["img1"]
        image2 = c["img2"]

        # Create the rows of the table, one row per question
        table_rows = ""
        notes = 0
        for q in c["questions"]:
            td1 = q[0]                              # question text
            td2 = y_icon if q[1] == "y" else n_icon # first icon
            td3 = y_icon if q[2] == "y" else n_icon # second icon
            notes1 = ""
            notes2 = ""
            for j in range(3, len(q)):
                note = q[j]
                if (note[0:3] == "c1:"):
                    notes += 1
                    notes1 = "<sup>" + str(notes) + "</sup>"
                if (note[0:3] == "c2:"):
                    notes += 1
                    notes2 = "<sup>" + str(notes) + "</sup>"
            table_rows += table_row_template.format(td1, td2, notes1, td3, notes2)

        # Add a final row with the sum of tick marks per column
        sum1 = sum( [1 for q in c["questions"] if q[1] == "y"] )
        sum2 = sum( [1 for q in c["questions"] if q[2] == "y"] )
        td1 = "Σύνολο"
        td2 = "<b>" + str(sum1) + "</b>"
        td3 = "<b>" + str(sum2) + "</b>"
        notes1 = ""
        notes2 = ""
        table_rows += table_row_template.format(td1, td2, notes1, td3, notes2)

        # If any question had a note, add a footer to the panel
        panel_footer = ""
        if (notes > 0):
            notes = 1
            notes_text = ""
            for q in c["questions"]:
                for j in range(3, len(q)):
                    note_text = q[j][4:]
                    notes_text += "<br>&nbsp;&nbsp;&nbsp;&nbsp;" + str(notes) + ". " + note_text
                    notes += 1
            panel_footer = panel_footer_template.format(notes_text)

        outFile.write(panel_template.format(panel_title, image1, title1, image2, title2, table_rows, panel_footer))

        outFile.write(carousel_item_footer)
        carousel_items += 1

    outFile.write(carousel_footer)
    
#===============================================================================
# addHtmlFooter()
#===============================================================================
def addHtmlFooter(outFile):

    html_footer = """
    <p style="text-align: center; margin: 10px">
      <a href="http://gmargari.github.io/"><img style="vertical-align:middle" src="../img/more_w.gif"></a>
    </p>

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
        addContent(outFile)
        addHtmlFooter(outFile)

if __name__ == "__main__":
    main()

