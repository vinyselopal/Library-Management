import { BrowserRouter, Routes, Route } from "react-router-dom";

import "./App.css";
import AddBooks from "./pages/AddBooks";
import SearchBooks from "./pages/SearchBooks";
import Layout from "./pages/Layout";
import IssueBook from "./pages/IssueBook";
import SearchMembers from "./pages/SearchMembers";
import BorrowHistory from "./pages/BorrowHistory";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="librarymanagement" element={<Layout />}>
          <Route path="search_books" element={<SearchBooks />} />
          <Route path="add_books" element={<AddBooks />} />
          <Route path="issue_book" element={<IssueBook />} />
          <Route path="search_members" element={<SearchMembers />} />
          <Route path="borrow_history" element={<BorrowHistory />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
