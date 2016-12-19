for i in EngWikiZip/*
do
  python2.7 WikiExtractor.py -o EnglishOutput/$i/ --no-templates $i
done
