#****************************************************
# Function for creating the
# web page to be displayed
def web_page():
    html_page = """
<!DOCTYPE html>  
 <html>  
  <head>  
  <meta name='viewport' content='width=device-width, initial-scale=1.0'/>  
  <script>   
   var ajaxRequest = new XMLHttpRequest();  
   
   function ajaxLoad(ajaxURL)  
   {  
    ajaxRequest.open('GET',ajaxURL,true);  
    ajaxRequest.onreadystatechange = function()  
    {  
     if(ajaxRequest.readyState == 4 && ajaxRequest.status==200)  
     {  
      var ajaxResult = ajaxRequest.responseText;  
      var tmpArray = ajaxResult.split("|");  
      document.getElementById('temp').innerHTML    = tmpArray[0];  
      document.getElementById('humi').innerHTML    = tmpArray[1];
      document.getElementById('itu').innerHTML     = tmpArray[2];
      document.getElementById('Dew').innerHTML     = tmpArray[3];
      document.getElementById('press').innerHTML   = tmpArray[4];
      document.getElementById('alt').innerHTML     = tmpArray[5];
      document.getElementById('press_I').innerHTML = tmpArray[6];
      document.getElementById('alt_I').innerHTML   = tmpArray[7];
      document.getElementById('air').innerHTML     = tmpArray[8]; 
     }
    }  
    ajaxRequest.send();  
   }  
     
   function updateSensors()   
   {   
     ajaxLoad('getData');   
   }  
     
   setInterval(updateSensors, 10000);  
    
  </script>  
    
    
  <title>PSoC6 Indoor Weather Station</title>  
  </head>  
    
  <body>  
   <center>  
   <div id='main'>  
    <h1>MicroPython Weather Station</h1>  
    <h4>Web server on PSoC6</h4>
    <h4>Sensor values auto updates using AJAX</h4>  
    <div id='content'>   
     <p>Temperature: <strong><span id='temp'>--.-</span> &deg;C</strong></p>  
     <p>Humidity: <strong><span id='humi'>--.-</span> % </strong></p>
     <p>Confort factor: <strong><span id='itu'>--.-</span> value </strong></p>
     <p>DEW point: <strong><span id='Dew'>--.-</span> &deg;C </strong></p>
     <p>Atmospheric pressure: <strong><span id='press'>--.-</span> mmHg </strong></p>
     <p>Relative altitude: <strong><span id='alt'>--.-</span> meters </strong></p>
     <p>Atmospheric pressure I: <strong><span id='press_I'>--.-</span> mmHg </strong></p>
     <p>Relative altitude I: <strong><span id='alt_I'>--.-</span> meters </strong></p>
     <p>Air CO2: <strong><span id='air'>--.-</span> ppm </strong></p>
    </div>  
   </div>  
   </center>  
  </body>  
 </html>
"""
    return html_page
#****************************************************