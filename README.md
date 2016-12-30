# WikiToJson
以下提供完成轉換的中英文wikiJson檔  
英文wiki的json檔https://drive.google.com/open?id=0ByoB_9NkZ9rRa1dLQjdYWlRQYm8  
中文wiki的json檔(裡面有部分文章語句為簡體中文)https://drive.google.com/open?id=0ByoB_9NkZ9rRa3VUY25TeXRtdnM  
繁體中文wiki的json檔https://drive.google.com/file/d/0ByoB_9NkZ9rRTm9UN3VJUjJqMkk/view?usp=sharing  
繁體中文wiki的json檔，且content經過斷詞https://drive.google.com/file/d/0ByoB_9NkZ9rRZWFRa1FiWlZYTDA/view?usp=sharing  

  
程式碼使用方法  
準備的資料用wiki資料庫下載  
中文https://dumps.wikimedia.org/zhwiki/  
英文https://dumps.wikimedia.org/enwiki/  
  
這裡使用的是 Articles, templates, media/file descriptions, and primary meta-pages.部分的檔案  
當下載下來的壓縮檔使用unzip的code先解壓縮到同一資料夾下  
  
<code>sh unzipall.sh 資料夾名  </code>
  
這個shell script 會呼叫WikiExtractor.py  
當解壓縮完，即可使用wikiToJson.py  

<code>python3 wikiToJson.py 來源資料夾名 輸出json的檔名  </code>

當完成json檔的工作，這裡有提供一個使用ijson搜尋工具，ijson主要是使用在json過大而不能夠全部loading進記憶體時，採用stream的方式讀取json檔。  

這裡提供原ijson的github: https://github.com/isagalaev/ijson  
  
<code>python3 ijsonSearch.py 查詢的json檔名 查詢的目標類型 查詢目標名稱  </code>

查詢目標類型有t, i參數，t為wiki文章的title；i為wiki文章的id  
範例:  
<code>python3 ijsonSearch.py WikiJson.json t 周杰倫  </code>
