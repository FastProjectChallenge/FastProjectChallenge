var helper = {

    data: 'what?',

    getData: function(URL) {
        $.getJSON(URL, function(json) {
            console.log(json);
            return (json);
        });
    },

    postData: function(URL, postData) {
        $.post(URL, postData, function(data) {
            console.log(data); // John
        }, "json");
    },
}