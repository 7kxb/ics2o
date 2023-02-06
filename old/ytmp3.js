var YoutubeMp3Downloader = require("youtube-mp3-downloader");
var YD = new YoutubeMp3Downloader({
    "ffmpegPath": "/bin/ffmpeg",
});
YD.download("8R5LYHX4Arc");
YD.on("finished", function(err, data) {
    console.log(JSON.stringify(data));
});