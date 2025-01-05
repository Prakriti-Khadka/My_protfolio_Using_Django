let searchBox = document.querySelector(".SearchPlace");
let searchBtn = document.querySelector(".Searchbutton");
let time = document.querySelector(".time");
let date = document.querySelector(".date");

function convertCountryCode(country) {
    let regionNames = new Intl.DisplayNames(["en"], { type: "region" });
    return regionNames.of(country);
}

function updateTime_Date() {
    const now = new Date();
    const options = { weekday: "long", month: "long", day: "numeric" };
    const formattedDate = now.toLocaleDateString("en-US", options);
    const formattedTime = now.toLocaleTimeString("en-US", { hour: "numeric", minute: "2-digit", hour12: true });

    time.textContent = formattedTime;
    date.textContent = formattedDate;
}

// Update time and date initially and every 200 milliseconds
updateTime_Date();
setInterval(updateTime_Date, 200);

async function checkWeather(city) {
    const Api_Key = "2293671f0c948d6ca4df54ad7a73e082";
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?units=metric&q=${city}&appid=${Api_Key}&units=metrics`);
    const data = await response.json();

//data.cod means any response from Api and if response not equal to 200 means there might be some error.
    if (data.cod && data.cod !== 200) {
        return;
    }

    document.querySelector('.icon img').src = `https://openweathermap.org/img/wn/${data.weather[0].icon}.png`;
    document.querySelector('.humidity').innerHTML = `${data.main.humidity}%`;
    document.querySelector('.pressure').innerHTML = `${data.main.pressure}hPa`;
    document.querySelector('.wind').innerHTML = `${data.wind.speed}m/s`;
    document.querySelector('.temp').innerHTML = `${data.main.temp}°C`;
    document.querySelector('.city').innerHTML = `${data.name}, ${convertCountryCode(data.sys.country)}`;
    document.querySelector('.weather_forecast').innerHTML = `${data.weather[0].description}`.toUpperCase();
}

checkWeather("Manchester");

searchBtn.addEventListener('click', function () {
    let cityName = searchBox.value;
    checkWeather(cityName);
});

searchBox.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        let cityName = searchBox.value;
        checkWeather(cityName);
    }
});
