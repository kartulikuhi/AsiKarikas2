PlayerLiftPotState = Class{__includes = BaseState}

function PlayerLiftPotState:init(player, dungeon)
	self.player = player
	self.dungeon = dungeon
	self.pot = self.dungeon.currentRoom.objects[2]
	self.player:changeAnimation('lift-pot-' .. self.player.direction)
end

function PlayerLiftPotState:enter()
	self.player.currentAnimation:refresh()
	self:raisePot()
end

function PlayerLiftPotState:update(dt)
	
	if self.player.currentAnimation.timesPlayed > 0 then
        self.player.currentAnimation.timesPlayed = 0
        self.player.carryingPot = true
        self.player:changeState('carry-pot-idle')
    end
end

function PlayerLiftPotState:raisePot()
	Timer.tween(0.3, {
		[self.pot] = {x = self.player.x + 4, y = self.player.y - self.pot.height + 4}
	})
	self.pot.solid = false
	self.pot.pickedUp = true
end

function PlayerLiftPotState:render()
    love.graphics.draw(gTextures[self.player.currentAnimation.texture], gFrames[self.player.currentAnimation.texture][self.player.currentAnimation:getCurrentFrame()],
        math.floor(self.player.x - self.player.offsetX), math.floor(self.player.y - self.player.offsetY))
end

