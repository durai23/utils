#script for 2 way mapping from alphanumeric to numeric over files in a dir
#create alpha and num array and then push num into alpha. push dot and underscore into alpha

alpha=("a".."z").to_a
num=("0".."9").to_a

for i in 0..(num.length-1)
  alpha.push(num[i])
end

alpha.push(".","_")

def textnum(d,c)
  Dir.chdir(d)
  n=0 # counter
  if c=="n"
    #get all filenames in present dir into an array
    fnames=Array.new
    Dir.foreach(".") { |f| 
      fnames.push("#{f}")
      nfname=Array.new
      puts "actual file name #{fnames[n]}"
    #split fnames into chars and push into nfname the corresponding number using index()  
      fnames[n].split("").each do |i|
        nfname.push(alpha.index(i.downcase)+1)
      end
    #if fnames entity then replace alpha fname with numeric code nfname else show error
      if "#{fnames[n]}" =~ /[^\.]/
        puts "changed file name #{nfname.join("_")}"
        File.rename("#{fnames[n]}","#{nfname.join("_")}")
      else 
        puts "ERROR"
      end
      n=n+1
    }
  else
    #get all filenames in present dir into an array
    nfnames=Array.new
    Dir.foreach(".") { |f| 
      next if f=='.' or f=='..'
      nfnames.push("#{f}")
      fnames=Array.new
      puts "actual file name #{nfnames[n]}"
      #split fnames into nums and push into fnames the corresponding char 
      nfnames[n].split("_").each do |i|
        j=i.to_i
        fnames.push(alpha[j-1])
      end
      puts "changed file name #{fnames.join("")}"
      File.rename("#{nfnames[n]}","#{fnames.join("")}")
      n=n+1
    }
  end
end

puts "enter path followed by 'n' for text to num and 'x' for num to text"
system 'cls'
textnum(ARGV[0],ARGV[1])

