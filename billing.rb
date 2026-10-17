def pay(amount)
  raise "neg" if amount < 0
  amount * 1.0
end
puts pay(10)
