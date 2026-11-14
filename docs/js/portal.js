/* Jhunjhunu Blog portal: weather, site search, fact filter. No trackers. */
(function () {
  var L = document.body.getAttribute('data-lang') || 'hi';
  var T = {
    hi: { now: 'अभी', hum: 'नमी', wind: 'हवा', max: 'अधिकतम', min: 'न्यूनतम', err: 'मौसम अभी लोड नहीं हो सका।', none: 'कोई नतीजा नहीं मिला। दूसरा शब्द आज़माएँ, या हमसे पूछें।', days: ['आज', 'कल', 'परसों'] },
    en: { now: 'Now', hum: 'Humidity', wind: 'Wind', max: 'High', min: 'Low', err: "Couldn't load the weather right now.", none: 'No results. Try another word, or ask us.', days: ['Today', 'Tomorrow', 'Day after'] }
  }[L];
  var WMO = { 0: ['☀️', 'साफ़', 'Clear'], 1: ['🌤️', 'ज़्यादातर साफ़', 'Mostly clear'], 2: ['⛅', 'आंशिक बादल', 'Partly cloudy'], 3: ['☁️', 'बादल', 'Cloudy'],
    45: ['🌫️', 'कोहरा', 'Fog'], 48: ['🌫️', 'कोहरा', 'Fog'], 51: ['🌦️', 'बूँदाबाँदी', 'Drizzle'], 53: ['🌦️', 'बूँदाबाँदी', 'Drizzle'], 55: ['🌦️', 'बूँदाबाँदी', 'Drizzle'],
    61: ['🌧️', 'हल्की बारिश', 'Light rain'], 63: ['🌧️', 'बारिश', 'Rain'], 65: ['🌧️', 'तेज़ बारिश', 'Heavy rain'], 80: ['🌦️', 'बौछारें', 'Showers'], 81: ['🌦️', 'बौछारें', 'Showers'], 82: ['⛈️', 'तेज़ बौछारें', 'Heavy showers'],
    95: ['⛈️', 'आँधी-तूफ़ान', 'Thunderstorm'], 96: ['⛈️', 'आँधी-तूफ़ान', 'Thunderstorm'], 99: ['⛈️', 'आँधी-तूफ़ान', 'Thunderstorm'] };
  function w(c) { var x = WMO[c] || ['🌡️', '', '']; return { i: x[0], t: L === 'hi' ? x[1] : x[2] }; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  var box = document.querySelector('[data-wx] .wx-body');
  if (box) {
    fetch('https://api.open-meteo.com/v1/forecast?latitude=28.13&longitude=75.40&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=Asia%2FKolkata&forecast_days=3')
      .then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function (d) {
        var c = d.current, n = w(c.weather_code), days = '';
        for (var i = 0; i < 3; i++) { var x = w(d.daily.weather_code[i]); days += '<li><span>' + T.days[i] + '</span><span aria-hidden="true">' + x.i + '</span><span>' + Math.round(d.daily.temperature_2m_max[i]) + '° / ' + Math.round(d.daily.temperature_2m_min[i]) + '°</span></li>'; }
        box.innerHTML = '<p class="wx-now"><span class="wx-ic" aria-hidden="true">' + n.i + '</span><span class="wx-t">' + Math.round(c.temperature_2m) + '°C</span></p><p class="wx-desc">' + esc(n.t) + ' · ' + T.hum + ' ' + c.relative_humidity_2m + '% · ' + T.wind + ' ' + Math.round(c.wind_speed_10m) + ' km/h</p><ul class="wx-days">' + days + '</ul>';
      })
      .catch(function () { box.innerHTML = '<p class="muted">' + T.err + '</p>'; });
  }

  var res = document.querySelector('[data-search]');
  if (res) {
    var q = (new URLSearchParams(location.search).get('q') || '').trim();
    var inp = document.getElementById('q'); if (inp) inp.value = q;
    if (q) {
      fetch('../../js/search-index.json').then(function (r) { return r.json(); }).then(function (idx) {
        var terms = q.toLowerCase().split(/\s+/).filter(Boolean), out = [];
        (idx[L] || []).concat(idx[L === 'hi' ? 'en' : 'hi'].map(function (p) { p.o = 1; return p; })).forEach(function (p) {
          var hay = (p.t + ' ' + p.d + ' ' + p.x).toLowerCase(), s = 0;
          terms.forEach(function (t) { if (hay.indexOf(t) > -1) s += 1; if (p.t.toLowerCase().indexOf(t) > -1) s += 3; });
          if (s >= terms.length) out.push([s - (p.o ? 2 : 0), p]);
        });
        out.sort(function (a, b) { return b[0] - a[0]; });
        var seen = {}, html = '';
        out.slice(0, 20).forEach(function (r) { var p = r[1], lang = p.o ? (L === 'hi' ? 'en' : 'hi') : L, href = '../../' + lang + '/' + p.u; if (seen[href]) return; seen[href] = 1;
          html += '<li><a href="' + href + '">' + esc(p.t) + '</a><p class="muted small">' + esc(p.d) + '</p></li>'; });
        res.innerHTML = html || '<li class="muted">' + T.none + ' <a href="../help/">→</a></li>';
      });
    }
  }

  var chips = document.querySelectorAll('.fact-filter [data-filter]');
  chips.forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.getAttribute('data-filter');
      chips.forEach(function (x) { x.classList.toggle('is-on', x === b); });
      document.querySelectorAll('.fact-grid .fact-card').forEach(function (c) { c.hidden = !!f && c.getAttribute('data-cat') !== f; });
    });
  });
})();
