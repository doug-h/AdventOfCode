#!/usr/bin/env ruby
# frozen_string_literal: true

D_NAMES = %w[\d one two three four five six seven eight nine]

def eval_line(line)
  matches = line.scan(/(?=(#{D_NAMES * '|'}))/)
  values = matches.map { |x,| D_NAMES.index(x) || x[0].to_i }
  values[0] * 10 + values[-1]
end

total = IO.foreach('data.txt').sum { |x| eval_line(x) }
puts total
