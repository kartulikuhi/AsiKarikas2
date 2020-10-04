PauseState = Class{__includes = BaseState}

local pausedbutton = love.graphics.newImage('paused.png')
function PauseState:init()
	self.countdown = 3
	self.countdowntimer = 0
end
function PauseState:enter(params)
	self.score = params.score
	self.pipePairs = params.pipePairs
	self.bird = params.bird
	self.timer = params.timer
	self.lastY = params.lastY
	scrolling = false
	wastitlescreen = false
end

function PauseState:update(dt)
	if love.keyboard.wasPressed('p') then
		gStateMachine:change('countdown', {
			score = self.score,
			pipePairs = self.pipePairs,
			bird = self.bird,
			timer = self.timer,
			lastY = self.lastY,
			counttime = 3
		})
		sounds['pause']:play()
	end
end

function PauseState:render()
	for k, pair in pairs(self.pipePairs) do
		pair:render()
	end

	love.graphics.setFont(flappyFont)
    love.graphics.print('Score: ' .. tostring(self.score), 8, 8)

    self.bird:render()

    love.graphics.draw(pausedbutton, VIRTUAL_WIDTH/2 - pausedbutton:getWidth()/2*0.3, 0, 0, 0.3, 0.3)
end


