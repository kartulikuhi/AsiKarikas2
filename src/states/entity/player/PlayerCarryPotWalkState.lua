PlayerCarryPotWalkState = Class{__includes = PlayerWalkState}

function PlayerCarryPotWalkState:init(entity, dungeon)
	self.entity = entity
	self.dungeon = dungeon
	self.pot = self.dungeon.currentRoom.objects[2]
	self.entity:changeAnimation('carry-pot-walk-' .. self.entity.direction)
end

function PlayerCarryPotWalkState:enter()
	self.entity.currentAnimation:refresh()
end

function PlayerCarryPotWalkState:update(dt)

	self.pot.x = self.entity.x + 4
	self.pot.y = self.entity.y - self.pot.height

	if love.keyboard.isDown('left') then
        self.entity.direction = 'left'
        self.entity:changeAnimation('carry-pot-walk-left')
    elseif love.keyboard.isDown('right') then
        self.entity.direction = 'right'
        self.entity:changeAnimation('carry-pot-walk-right')
    elseif love.keyboard.isDown('up') then
        self.entity.direction = 'up'
        self.entity:changeAnimation('carry-pot-walk-up')
    elseif love.keyboard.isDown('down') then
        self.entity.direction = 'down'
        self.entity:changeAnimation('carry-pot-walk-down')
    else
        self.entity:changeState('carry-pot-idle')
    end
    EntityWalkState.update(self, dt)

    if love.keyboard.wasPressed('f') then
    	self:throwPot()
    	self.entity:changeState('walk')
    end
end

function PlayerCarryPotWalkState:throwPot()
	if self.entity.direction == 'left' then
		self.pot.thrown = true

		Timer.tween(0.5, {
			[self.pot] = {x = self.pot.x - TILE_SIZE*4}
		}):finish(function()
			table.remove(self.dungeon.currentRoom.objects, 2)
		end)

	elseif self.entity.direction == 'right' then
		self.pot.thrown = true

		Timer.tween(0.5, {
			[self.pot] = {x = self.pot.x + TILE_SIZE*4}
		}):finish(function()
			table.remove(self.dungeon.currentRoom.objects, 2)
		end)

	elseif self.entity.direction == 'down' then
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


function PlayerCarryPotWalkState:render()

	love.graphics.draw(gTextures[self.entity.currentAnimation.texture], gFrames[self.entity.currentAnimation.texture][self.entity.currentAnimation:getCurrentFrame()],
        math.floor(self.entity.x - self.entity.offsetX), math.floor(self.entity.y - self.entity.offsetY))
end