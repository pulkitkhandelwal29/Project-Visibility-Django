// Primary loader Function to Start the Process
window.addEventListener("load", () => {
  audioCheck();
});

// Double CLick to Restart the Process
window.addEventListener("dblclick", () => {
  playDefaultAudio();
});

const audioCheck = () => {
  // Check if there is any Audio to be played or user wants to exit
  let pageAudio = document.querySelector("#python-audio");
  if (pageAudio.getAttribute("src") === "stop") {
    // Tell user they have stopped and how to start again
    const stopAudio = document.querySelector("#stop-audio");
    stopAudio.play();
    stopAudio.addEventListener("ended", () => {
      let pageAudio = document.querySelector("#python-audio");
      if (pageAudio.getAttribute("src") !== "") {
        pageAudio.setAttribute("src", "");
      }
    });
  } else {
    // If a audio src exist play it first
    if (pageAudio.getAttribute("src") !== "") {
        pageAudio.play();
        pageAudio.addEventListener("ended", playDefaultAudio);
      // pageAudio.play();
      // pageAudio.addEventListener("ended", playDefaultAudio);
    } else {
      playDefaultAudio();
    }
  }
};

// Default Audio function
const playDefaultAudio = () => {
  // If Src exist in Dynamic Audio it is removed
  // Checking if audio src exist
  let pageAudio = document.querySelector("#python-audio");
  if (pageAudio.getAttribute("src") !== "") {
    pageAudio.setAttribute("src", "");
  }
  //get audio by id
  const initial = document.querySelector("#initial-audio");
  initial.play();
  //Start Recording after the audio stops
  initial.addEventListener("ended", runSpeechRecognition);
};

// Speech Recognition function
function runSpeechRecognition() {
  // get output div reference
  var output = document.getElementById("output");

  // new speech recognition object
  var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
  var recognition = new SpeechRecognition();

  // This runs when the speech recognition service returns result
  recognition.onresult = function (event) {
    // Transcript is the string and confidence is surety of machine
    var transcript = event.results[0][0].transcript;
    var confidence = event.results[0][0].confidence;
    // Append text to the form and submit
    let autoFormSubmit = document.querySelector("#express");
    // <!-- Adding user input and machine confidence in inputs -->
    document.querySelector("#user-text").value = transcript;
    document.querySelector("#user-confidence").value = confidence;
    document.querySelector("#current-url").value = window.location.href;
    console.log(
      `This is the string : ${transcript}, the confidence ${confidence}`
    );
    // Submitting the form
    autoFormSubmit.submit();
  };

  // start recognition
  recognition.start();
}
