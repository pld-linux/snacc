Summary:	SNACC - ASN.1 to C or C++ compiler
Summary(pl.UTF-8):	SNACC - Kompilator ASN.1 do C lub C++
Name:		snacc
Version:	1.3
Release:	0.1
License:	GPL v2
Group:		Development/Tools
Source0:	http://ftp.debian.org/debian/pool/main/s/snacc/%{name}_%{version}bbn.orig.tar.gz
#http://ftp.debian.org/debian/pool/main/s/snacc/snacc_1.3bbn-9.diff.gz
Patch0:		%{name}_1.3bbn-9.diff
URL:		http://directory.fsf.org/GNU/snacc.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snacc is short for "Sample Neufeld ASN.1 to C Compiler" and ASN.1
stands for Abstract Syntax Notation One (ITU-T X.208/ISO 8824). Snacc
supports a subset of ASN.1 1988. If you need features of ASN.1 1992 or
later, snacc is not for you.

Given an ASN.1 source file(s) snacc can produce: 1. C routines for BER
encoding, decoding, printing and freeing. 2. C++ routines for BER
encoding, decoding, and printing. 3. A type table that can be used
with C driver routines for BER encoding, decoding, printing and
freeing.

%description -l pl.UTF-8
Snacc jest skrótem od "Sample Neufeld ASN.1 to C Compiler", a ASN.1 to
"Abstract Syntax Notation One" (ITU-T X.208/ISO 8824). Snacc wspiera
podzbiór ASN.1 1988. Jeśli potrzebujesz właściwości ASN.1 1992 lub
późniejszych to snacc nie jest dla Ciebie.

Na podstawie pliku(ów) źródłowego ASN.1 snacc może stworzyć: 1.
funkcje C do kodowania, deokodowania, wypisywania i zwalniania BER 2.
funkcje C++ do kodowania, deokodowania, wypisywania i zwalniania BER
3. tabelę typów, której można używać z funkcjami C do kodowania,
dekodowania, wypisywania i zwalniania

%if %{with devel-static}
%package devel
Summary:	Development libraries and header files for SNACC library
Group:		Development/Libraries

%description devel
This is the package containing the development libraries and header
files for SNACC

%package static
Summary:	Static SNACC library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SNACC library.

%endif

%prep
%setup -q -n %{name}-%{version}bbn.orig
%patch -P0 -p0

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif

#%{_examplesdir}/%{name}-%{version}
