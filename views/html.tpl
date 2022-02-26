% import os
<!DOCTYPE html>
<html lang="en/US">
<head>
<meta charset="utf-8">
<!--
	width=device-width			sets the width of the page to follow the screen-width of the device
	initial-scale=1.0			sets the initial zoom level when the page is first loaded by the browser
-->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{title}}</title>
<link rel="stylesheet" href="/css/normalize.css">
% if not css is None and type(css).__name__ == 'list':
%	for sheet in css:
<link rel="stylesheet" media="screen" href="/css/{{sheet}}">
%	end
% end
<!--<link rel="stylesheet" media="print" href="print.css">-->
% if not javascript is None and type(javascript).__name__ == 'list':
%	for script in javascript:
<script src="/javascript/{{script}}"></script>
%	end
% end
</head>
<body>
{{!content if content else "No content is defined."}}
</body>
</html>