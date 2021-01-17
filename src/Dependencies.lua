Class = require 'lib/class'
Event = require 'lib/knife.event'
push = require 'lib/push'
Timer = require 'lib/knife.timer'

require 'src/constants'
require 'src/StateMachine'
require 'src/Board'
require 'src/Coin'

require 'src/States/BaseState'
require 'src/States/game/StartState'
require 'src/States/game/PlayState'
require 'src/States/game/GameOverState'


gTextures = {
    ['board'] = love.graphics.newImage('graphics/board.png'),
    ['red_coin'] = love.graphics.newImage('graphics/redcoin.png'),
    ['yellow_coin'] = love.graphics.newImage('graphics/yellowcoin.png'),
    ['background'] = love.graphics.newImage('graphics/background.png')
}

gFonts = {
    ['small'] = love.graphics.newFont('fonts/Roboto-Black.ttf', 16),
    ['medium'] = love.graphics.newFont('fonts/Roboto-Black.ttf', 32),
    ['large'] = love.graphics.newFont('fonts/Roboto-Black.ttf', 64)
    
}

gSounds = {
    ['music'] = love.audio.newSource('sounds/music.mp3'),
    ['error'] = love.audio.newSource('sounds/error.wav'),
    ['selection'] = love.audio.newSource('sounds/swap_selection.wav'),
    ['coin'] = love.audio.newSource('sounds/coin_drop.wav'),
    ['win'] = love.audio.newSource('sounds/win.wav')
}