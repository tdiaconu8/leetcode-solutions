class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = [homepage]
        self.len = 1
        self.i = 0

    def visit(self, url: str) -> None:
        if self.i + 1 > len(self.browser) - 1:
            self.browser.append(url)
        self.i += 1
        self.len = self.i+1
        self.browser[self.len-1]=url

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self.browser[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.len - 1, self.i + steps)
        return self.browser[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
