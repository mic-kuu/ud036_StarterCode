import webbrowser
import os

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>mic-kuu's favourite movies</title>
  <link href="https://fonts.googleapis.com/css?family=Josefin+Sans" rel="stylesheet">
</head>
<body>
'''

# Site's style (we're adding panel's backgrounds here)
style = '''
  <style>
    html {{
      box-sizing: border-box;
      font-family: 'Josefin Sans', sans-serif;
    }}
    body {{
      margin: 0;
    }}
    .panels {{
      min-height:100vh;
      overflow: hidden;
      display: flex;
    }}
    .panel {{
      color: white;
      text-align: center;
      align-items: center;
      transition:
        font-size 1.5s cubic-bezier(0.6,-0.15, 0.8,-0.2),
        flex 1.5s cubic-bezier(0.6,-0.15, 0.8,-0.2);
      background-size:cover;
      background-position:center;
      flex: 1;
      justify-content: center;
      display: flex;
      flex-direction: column;
    }}

    {panel_backgrounds}

    /* Apply to all children elements of class panel */
    .panel > * {{
      margin:0;
      width: 100%;
      transition:transform 0.5s;
      flex: 1 0 auto;
      display:flex;
      justify-content: center;
      align-items: center;
      font-size: 2em;
    }}
    /* Move title up on activation and then back on deactivation */
    .panel > *:first-child {{ transform: translateY(20%); }}
    .panel.open-active > *:first-child {{ transform: translateY(-5%); }}

    .panel.open-active > *:last-child {{ transform: translateY(0); }}
    /* Hide video before activation and show it when activated */
    .panel > *:last-child {{ transform: translateY(100%); }}
    .panel.open-active > *:last-child {{ transform: translateY(0); }}

    .panel p {{
      text-transform: lowercase;
      text-shadow: 0 0 8px rgba(0, 0, 0, 0.9), 0 0 20px rgba(0, 0, 0, 0.5);
      font-size: 3em;
    }}

    .panel.open {{
      flex: 2;
      font-size: 2em;
    }}

    /* Added to responsively resize embeded youtube video's */
    .videoWrapper {{
    	position: relative;
    	padding-bottom: 56.25%; /* 16:9 */
    	padding-top: 0px;
    	height: 0;
    }}
      /* Added to responsively resize embeded youtube video's */
    .videoWrapper iframe {{
    	position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%,-50%);
    	width: 70%;
    	height: 70%;
    }}

  </style>
'''

# Page's main content - we're adding rendered styles and movie's html code here
main_page_content = '''
    {style}
    <div class="panels">
    {movie_panels}
    </div>
'''
# Remaining JS and HTML - responsible mostly for click events on the page
page_scripts = '''
  <script>
    const panels = document.querySelectorAll('.panel');

    // Add or remove open class to panels on click
    function toggleOpen() {
      this.classList.toggle('open');

      //iterate over all panels and close all other than the clicked one
      panels.forEach( (panel) => {
          if (panel !== this){
            panel.classList.remove('open');
          }
      } )
    }
    panels.forEach(panel => panel.addEventListener('click', toggleOpen));

    // When panel has finished opening - transition the video
    function toggleActive(e) {
      if (e.propertyName.includes('flex')) {
        this.classList.toggle('open-active');
      }
    }
    panels.forEach(panel => panel.addEventListener('transitionend', toggleActive));

  </script>

</body>
</html>
'''

# Template for setting background of movie panels (
poster_background_css = ''' .panel{movie_no} {{background-image:url({poster_url}); }} '''

# HTML template for each movie
poster_panel = '''
    <div class="panel panel{movie_no}">
      <p>{movie_title}</p>
      <div class="videoWrapper">
        <iframe width="560" height="315" src="{trailer_youtube_url}" frameborder="0" allowfullscreen></iframe>
      </div>
    </div> '''


# Renders CSS part of each movie - background for each panel
def create_panel_backgrounds(movies):
    panel_backgrounds = ''
    for index, movie in enumerate(movies):
        # Add new css class containg the poster background (panel1, panel2, panel3...)
        panel_backgrounds += poster_background_css.format(movie_no=index, poster_url=movie.poster_image_url)

    return panel_backgrounds

# Renders HTML part of each movie - divs with title and youtube link
def create_movie_panels(movies):
    panels = ''
    for index, movie in enumerate(movies):
        panels += poster_panel.format(
            movie_no=index,
            movie_title=movie.title,
            trailer_youtube_url=movie.trailer_youtube_url
        )

    return panels


def generate_and_open(movies):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # generate project style (background for consecutive panels)
    rendered_style = style.format(
        panel_backgrounds=create_panel_backgrounds(movies))

    # generate divs containg movie html
    rendered_content = main_page_content.format(
        style=rendered_style,
        movie_panels=create_movie_panels(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content + page_scripts)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
