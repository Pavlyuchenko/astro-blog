// DD/MM/YYYY HH:MM:SS to milliseconds

function convertDateToMilliseconds(date) {
    var date = new Date(date);
    console.log(date);

    return date.getTime();
}

new Date("05/01/2023 20:00:00").getTime();

setTimeout(() => {
    location.reload();
    // Example: 05/01/2023 20:00:00
}, new Date("MM/DD/YYYY HH:MM:SS").getTime() - Date.now());
