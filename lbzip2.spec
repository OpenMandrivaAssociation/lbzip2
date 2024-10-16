Name:           lbzip2
Version:        2.5
Release:        3
Summary:        Fast, multi-threaded bzip2 utility
Group:          Archiving/Compression
License:        GPLv2+
URL:            https://lbzip2.org/
Source0:	http://archive.lbzip2.org/%{name}-%{version}.tar.gz

BuildRequires:  bzip2-devel >= 1.0.6, dash, sharutils

%description
lbzip2 is a multi-threaded implementation of bzip2, suited for serial and
parallel processing.  On a multi-core computer, lbzip2 is commonly
the fastest bzip2 decompressor for most bz2 files found on the internet.
(On dual-core computers, the 7za utility from the p7zip package may prove
more efficient.)

lbzip2 integrates nicely with GNU tar. Even on single-core computers, lbzip2
can speed up archiving in combination with tar, because lbzip2 allows
compression to overlap with disk usage to a greater extent than bzip2 does.


%prep
%setup -q

%build
%global optflags %{optflags} -Ofast
%configure
%make

%install
%makeinstall_std

%files
%doc ChangeLog README
%{_bindir}/%{name}
%{_bindir}/lbzcat
%{_bindir}/lbunzip2
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/lbzcat.1*
%doc %{_mandir}/man1/lbunzip2.1*
