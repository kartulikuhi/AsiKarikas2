PlayerCarryPotIdleState = Class{__includes = PlayerIdleState}

function PlayerCarryPotIdleState:init(player, dungeon)
	self.player = player
	self.dungeon = dungeon
	self.pot = self.dungeon.currentRoom.objects[2]
	self.player:changeAnimation('carry-pot-idle-' .. self.player.direction)
end

function PlayerCarryPotIdleState:enter()
	self.player.currentAnimation:refresh()
end

function PlayerCarryPotIdleState:update(dt)

	self.pot.x = self.player.x + 4
	self.pot.y = self.player.y - self.pot.height

	if love.keyboard.isDown('left') or love.keyboard.isDown('right') or
       love.keyboard.isDown('up') or love.keyboard.isDown('down') then
       self.player:changeState('carry-pot-walk')
    end

    if love.keyboard.wasPressed('f') then
    	self:throwPot()
    	self.player:changeState('idle')
    end
end

function PlayerCarryPotIdleState:render()
	love.graphics.draw(gTextures[self.player.currentAnimation.texture], gFrames[self.player.currentAnimation.texture][self.player.currentAnimation:getCurrentFrame()],
	    math.floor(self.player.x - self.player.offsetX), math.floor(self.player.y - self.player.offsetY))
end

function PlayerCarryPotIdleState:throwPot()
	if self.player.direction == 'left' then
		self.pot.thrown = true

		Timer.tween(0.5, {
			[self.pot] = {x = self.pot.x - TILE_SIZE*4}
		}):finish(function()
			table.remove(self.dungeon.currentRoom.objects, 2)
		end)

	elseif self.player.direction == 'right' then
		self.pot.thrown = true

		Timer.tween(0.5, {
			[self.pot] = {x = self.pot.x + TILE_SIZE*4}
		}):finish(function()
			table.remove(self.dungeon.currentRoom.objects, 2)
		end)

	elseif self.player.direction == 'down' then
		self.pot.thrown = true

		Timer.tween(0.5, {
			[self.pot] = {y = self.pot.y + TILE_SIZE*4}
		}):finish(function()
			table.remove(self.dungeon.currentRoom.objects, 2)
		end)
		
	else
		self.pot.thrown = true

		Timer.tween(0.5, {
			[self.pot] = {y = self.pot.y - TILE_SIZE*4}
		}):finish(function()
			table.remove(self.dungeon.currentRoom.objects, 2)
		end)

	end
end