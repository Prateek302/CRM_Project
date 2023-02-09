var imgname=["image1.jpg","image2.jpg","image3.jpg","image4.jpg"];
        var i=0;
        baseUrl="/static/images/";
        function moveSlider(){
         if(i==imgname.length)
          {
          i=0;
          }
          document.getElementById("slide").src=baseUrl+imgname[i];
          i++;
          window.setTimeout("moveSlider()",1000);
        }

