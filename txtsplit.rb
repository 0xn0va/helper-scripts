# # text = File.read('txtmatn.txt')
# # text.scan(/.{4}/)
# # put text
# # "abcd1234beefcake".scan(/.{4}/)
#
# # file='txtmatn.txt'
# # # file.scan(/.{4}/)
# # # puts file
# # #
# # File.readword(file).each do |word|
# #   word.scan(/.{4}/)
# #   puts word
# # end
#
# File.open('txtmatn.txt').read() =~ /.{4}/

text = File.read "txtmatn.txt"
puts "#{text.scan(/.{4}/).size} lines."
paragraphs = text.split ".\n"
puts "#{paragraphs.length} paragraphs."

words_in_each_paragraph = paragraphs.map.with_index do |paragraph, i|
#    puts "working on paragraph ##{i}"
    paragraph.scan(/.{4}/).map.with_index do |line, j|
   #     puts "working on line ##{j}"
        line.scan(/\w+/).tap &method(:p)
    end
end

p words_in_each_paragraph[1]