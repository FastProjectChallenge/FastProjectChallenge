<!DOCTYPE html>
<html>

<head>
    <title>Anymeter</title>

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">

    <!-- Custom styles for this template -->
    <link href="css/cover.css" rel="stylesheet">
    <link href="css/cover_change.css" rel="stylesheet">

    <script type="text/javascript" src="js/lib/jquery-1.11.1.min.js"></script>
    <!--jquery-->
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.2.9/angular.min.js"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.2.9/angular-route.js"></script>

    <!--angular-->

    <script type="text/javascript" src="js/helper.js"></script>
    <script type="text/javascript" src="js/app.js"></script>
</head>

<body>

    <div class="site-wrapper" ng-app="anymeterApp">

        <div class="site-wrapper-inner">

            <div class="cover-container">

                <div class="masthead clearfix">
                    <div class="inner">
                        <!--h3 class="masthead-brand">Anymeter</h3-->
                        <a href="#" class="dropdown-toggle lol masthead-brand" data-toggle="dropdown">Anymeter <span class="caret"></span></a>
                        <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
                            <li class="active" role="presentation"><a role="menuitem" tabindex="-1" href="#">Top</a>
                            </li>
                            <li role="presentation"><a role="menuitem" tabindex="-1" href="#">Last</a>
                            </li>
                            <li role="presentation"><a role="menuitem" tabindex="-1" href="#">Something else here
</a>
                            </li>
                            <li role="presentation" class="divider"></li>
                            <li role="presentation"><a role="menuitem" tabindex="-1" href="#">Separated link</a>
                            </li>
                        </ul>
                        
                        <ul class="nav masthead-nav">
                            <li class="active"><a href="http://getbootstrap.com/examples/cover/#">Sing In</a>
                            </li>
                            <li><a href="http://getbootstrap.com/examples/cover/#">Sing Up</a>
                            </li>
                            <li><a href="http://getbootstrap.com/examples/cover/#">About</a>
                            </li>
                            <li><a href="http://getbootstrap.com/examples/cover/#">Contact</a>
                            </li>
                        </ul>
                    </div>
                </div>

                <div ng-controller="anymeterTopListCtrl as Top" class="list-group top">
                    <h1 class="top-heading">Top 20</h1>
                    <li ng-repeat="top in Top.toppers" class="list-group-item">
                        <a href="http://getbootstrap.com/examples/cover/#" ><h3 class="top-heading ">Topper: {{top.name}}</h3></a>
                        <img ng-src="{{top.image}}" />
                        <p class="top-description">Description: {{top.description}}</p>
                        <p class="top-description">Rating: {{top.vote}}</p>
                        <!-- <p> <a href="http://getbootstrap.com/examples/cover/#" class="btn btn-lg btn-default">Learn more</a>
                    </p>-->
                    </li>
                </div>
                <!--<div class="inner cover">
            <h1 class="cover-heading">Wellcome to Anymeter!</h1>
            <p class="lead">Cover is a one-page template for building simple and beautiful home pages. Download, edit the text, and add your own fullscreen background photo to make it your own.</p>
            <p class="lead">
              <a href="http://getbootstrap.com/examples/cover/#" class="btn btn-lg btn-default">Learn more</a>
            </p>
          </div>-->

                <div class="mastfoot">
                    <!--<div class="inner">
                        <p>Cover template for <a href="http://getbootstrap.com/">Bootstrap</a>, by <a href="https://twitter.com/mdo">@mdo</a>.</p>
                    </div>-->
                </div>

            </div>

        </div>

    </div>

</body>

</html>
