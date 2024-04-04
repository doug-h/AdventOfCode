#!/usr/bin/env ruby
# frozen_string_literal: true

MAX = { 'blue' => 14, 'green' => 13, 'red' => 12 }

def eval_line(line)
  MAX.keys.to_h { |colour| [colour, line.scan(/(\d+) #{colour}/).map { |n,| n.to_i }.max] }
end

part_one = 0
part_two = 0
IO.foreach('data.txt').with_index(1) do |line, game_id|
  max_cubes = eval_line(line)
  part_one += max_cubes.all? { |colour, count| count <= MAX[colour] } ? game_id : 0
  part_two += max_cubes.values.inject(:*)
end
puts "Part one: #{part_one}"
puts "Part two: #{part_two}"
