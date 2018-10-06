READ_PATH = "../Text_data/tweetData.txt"
WRITE_PATH = "../Text_data/labelAttachDataRuby.txt"

#書き込み
def write(text)
  File.open(WRITE_PATH,"a") do |f|
    f.puts(text)
  end
end


#label付け
def label(text)
  labelName = "皮肉"
  pushLabel = "__label__#{labelName},#{text}"
  write(pushLabel)
end

#判断
def judge(text)
  puts "Q.#{text}は皮肉ですか？"
  print "(yes:1 / no:2) >>"
  result = gets.downcase.to_i
  if result == 1 then
    label(text)
    puts "\n「#{text}」を皮肉に分類しました。"
    puts "---------------------"
  elsif result == 2 then
    puts "\n「皮肉に分類しませんでした。」"
    puts "---------------------"
  else
    puts "\n1か2を入力してください。スキップします。"
    puts "---------------------"
  end
end

#tweetを一行ずつ表示
def tweet()
  File.open(READ_PATH,"r:utf-8") do |tweet|
    tweet.each_line do |line|
      judge(line.chomp)
    end
  end
end

if __FILE__ == $0
  tweet()
end
