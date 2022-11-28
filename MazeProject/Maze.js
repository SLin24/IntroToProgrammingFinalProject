// https://www.javatpoint.com/javascript-create-and-download-csv-file
// create CSV file data in an array  
// Paste in Inspect Element Console to download a csv file of the maze

    
//create a user-defined function to download CSV file   
function download_csv_file() {  
  
    //define the heading for each row of the data  
    var csv = ''
    //store each node as a binary string from 0 to 15 inclusive UDLR
    //merge the data with CSV  
   for (var i = 0; i < game[gameHeightAt]; i++) {
        for (var j = 0; j < game[gameWidthAt]; j++) {
            var node = i * game[gameWidthAt] + j;
            var num = 8 * maze[node][1] + 4 * maze[node][2] + 2 * maze[node][3] + maze[node][4];
            if (j != game[gameWidthAt] - 1) {
                csv += num + ",";
            } else {
                csv += num;
            }
        }
        csv += '\n';
   }
   
  
     
    var hiddenElement = document.createElement('a');  
    hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);  
    hiddenElement.target = '_blank';  
      
    //provide the name for the CSV file to be downloaded  
    hiddenElement.download = 'MazeData.csv';  
    hiddenElement.click();  
}  
download_csv_file()
