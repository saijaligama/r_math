<?php include("header.php"); ?>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title> **DECIMAL NUMBERS**</title>

    <link rel="stylesheet" type="text/css" href="/uncg_math/static/Geometry_files/mystyle.css">
    <meta name="description" content="Regular polygon, Trangle,
              Quadrilateral, Rectangle, Rombus, Trapezoid,
              Circle, Circular Segment/Sector, Prism, Pyramid,
              Cylinder, Cone, Sperical Cap/Sector">
    <script src="/uncg_math/static/Geometry_files/geometry.js"></script>
<style>
    .text_box_st {
        padding: 1px !important;
        width: 90px !important;
    }

    .text_box_st2 {
        padding: 3px !important;
        width: 90px !important;
    }
</style>
</head>


    <div class="example" style="height: 100% !important;">
        <div id="nav" style="clear:both;">
            <h1 style="color: white;text-align: center;"> Integer Numbers </h1>

            <ul style="margin-top: -20px;">
                <li style="padding-left: 179px;"><a href="/uncg_math">Home</a></li>

            </ul>
            
        </div>
<h2 style="text-align:center">First Grade EOG 1</h2>
<input type="button" class="btn btn-success" value="Open Question Steet" onClick="window.open('question/2014_2015_1st_Mid_Year_Student_Booklet.pdf');">
<form action="" method="POST">
    <button style="margin-top: -34px;margin-left: 171px;" class="btn btn-info" name="click" class="click">Start Test</button>
</form>
<?php
if(isset($_POST['click']))
{
  $date_clicked = time();
  //  $date_clicked = date('Y-m-d H:i:s');
	echo "You can Fill Box Now";
	
}?>

<form action="/uncg_math/templates/kindergarden_answer.php" method="POST">
<table border=0 width=100% bgcolor=moccasin>

<div class='col-md-6'>
<tr>
<td>
<h3>Task1</h3>
<div style="margin-left:5%">

1&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='18' size='18'><br><br/>
2&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'>&nbsp;&nbsp;Triangles<br><br/>
</div>
</td>
</tr>

<tr>
<td>
<h3>Task2</h3>
<div style="margin-left:5%">
1&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
2&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
3&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
4&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'><br><br/>
</div>
</tr>
</td>


<tr>
<td>
<h3>Task3</h3>
<div style="margin-left:5%">
1&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'>&nbsp;&nbsp;Red Apple<br><br/>
</div>
</tr>
</td>



<tr>
<td>
<h3>Task4</h3>
<div style="margin-left:5%">
1&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'>&nbsp;&nbsp;Children<br><br/>
</div>
</tr>
</td>



<tr>
<td>
<h3>Task5</h3>
<div style="margin-left:5%">
1&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'>&nbsp;&nbsp;Paint Brashes<br><br/>
</div>

</td>
</tr>


<tr>
<td>
<h3>Task6</h3>
<div style="margin-left:5%">
1&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'>&nbsp;&nbsp;Pancils<br><br/>
</div>

</td>
</tr>



<tr>
<td>
<h3>Task7</h3>
<div style="margin-left:5%">
1&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='2' size='2'>&nbsp;&nbsp;Rocks<br><br/>
</div>
</td>
</tr>

<tr>
<td>
<h3>Task8</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='5' size='2'><br><br/>
b&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='5' size='2'><br><br/>
c&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='5' size='2'><br><br/>
</div>

</td>
</tr>


<tr>
<td>
<h3>Task9</h3>
<div style="margin-left:5%">
a&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
b&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
c&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
d&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
e&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
f&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
g&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
h&nbsp;&nbsp;&nbsp;<input type='text' name='ques[]' maxlength='3' size='3'><br><br/>
</div>
</td>
</tr>



</table>
<input type='hidden' name='stime' value="<?php echo $date_clicked;?>">
    <button name="res" class="big btn btn-primary">Submit Answer</button>
</form>
