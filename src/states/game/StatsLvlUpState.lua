StatsLvlUpState = Class{__includes = BaseState}

function StatsLvlUpState:init(def)
    self.menu = def
end

function StatsLvlUpState:update(dt)
    self.menu:update(dt)
end

function StatsLvlUpState:render()
    self.menu:render()
end